from typing import List, Sequence, Tuple
import cv2
from PIL import Image
import numpy as np
from common.models.detector import DetectContourNode
from common.rpc.detector_pb2 import DetectContour
from common.utils.imaging import ImageGrid
import logging

log = logging.getLogger(__name__)


class ContourController:
    
    @staticmethod 
    def build_contour_tree(edges,img,contours, hierarchy) -> List[DetectContourNode]:
        '''
        Generates a nested list of contours
        '''
        width, height = img.size
        hierarchy = hierarchy[0]  # Get the actual array from shape (1, N, 4)
        max_area = (width * height) / 100
        nodes: List[DetectContourNode] = []
        for i,cnt in enumerate(contours):
            area = cv2.contourArea(cnt)
        
            x,y,w,h = cv2.boundingRect(cnt)
            area_confidence = min (area/max_area,1.0)
            if w <=0 or h<=0:
                continue
            
            roi_edges = edges[y:y+h,x:x+w]
            edge_strength = np.mean(roi_edges)/255.0 if roi_edges.size > 0 else 0.0
            conf = 0.7 * area_confidence + 0.3 * edge_strength
            x_rel = x/width
            y_rel = y/height
            w_rel = w/width
            h_rel = h/height
            nodes.append(DetectContourNode(index=i,x=x_rel,y=y_rel,w=w_rel,h=h_rel,confidence=conf))
    
        root_nodes:List[DetectContourNode] = []

        for i, h in enumerate(hierarchy):
            parent_idx = h[3]  # Parent index
            if parent_idx != -1:
                nodes[parent_idx].add_child(nodes[i])
            else:
                # No parent => root contour
                root_nodes.append(nodes[i])
        
        return root_nodes
    
    @staticmethod
    def build_contours(img,edges,contours) -> List[DetectContour]:
        width, height = img.size
        grid = ImageGrid(width, height)
        elements = []
        max_area = (width * height) / 100
        boxes=[]
        matches = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:
                x,y,w,h = cv2.boundingRect(contour)
                area_confidence = min (area/max_area,1.0)
                if w <=0 or h<=0:
                    continue
                
                roi_edges = edges[y:y+h,x:x+w]
                edge_strength = np.mean(roi_edges)/255.0 if roi_edges.size > 0 else 0.0
                confidence = 0.7 * area_confidence + 0.3 * edge_strength
                
                boxes.append((x, y, w, h))
                matches.append((x, y, w, h,confidence))
        log.debug("Found contours: {0}".format(len(boxes)))
        if len(boxes) > 1:
            best_rows, best_cols = grid.optimal_grid_size(boxes)
        for box in matches:
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            conf = box[4]
            if len(boxes) > 1:
                row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)
            else:
                row = 0
                col = 0
                    
            x_rel = x/width
            y_rel = y/height
            w_rel = w/width
            h_rel = h/height
            elements.append(DetectContour(x=x_rel,y=y_rel,w=w_rel,h=h_rel,confidence=conf,row=row,col=col))
        return elements
    
    @staticmethod
    def detect_contours(img:Image):
        imgGray = img.convert('L')
        grayImg = np.array(imgGray)
        blurred = cv2.GaussianBlur(grayImg,(5,5),0)
        med_val = np.median(grayImg) 
        lower = int(max(0 ,0.7*med_val))
        upper = int(min(255,1.3*med_val))
        edges = cv2.Canny(blurred,lower,upper)
        
        contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        return edges,contours,hierarchy
    
    @staticmethod 
    async def print_tree(node, level=0):
        print("  " * level + f"Contour {node.index}, Children: {len(node.children)}")
        for child in node.children:
            ContourController.print_tree(child, level + 1)