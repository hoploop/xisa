import { KeyComboPressEventTypeEnum, KeyTypeEventTypeEnum, MouseClickEventTypeEnum, MouseDoubleClickEventTypeEnum, MouseDropEventTypeEnum, MousePressEventTypeEnum, MouseReleaseEventTypeEnum } from "@api/index";
import { KeyPressEventTypeEnum } from '@api/model/key-press-event';
import { KeyReleaseEventTypeEnum } from '@api/model/key-release-event';
import { MouseScrollEventTypeEnum } from '@api/model/mouse-scroll-event';

export enum RecordEventTypes {
  KeyComboPress = KeyComboPressEventTypeEnum.KeyComboPress,
  KeyPress = KeyPressEventTypeEnum.KeyPress,
  KeyType = KeyTypeEventTypeEnum.KeyType,
  KeyRelease = KeyReleaseEventTypeEnum.KeyRelease,
  MouseDroop = MouseDropEventTypeEnum.MouseDrop,
  MouseClick = MouseClickEventTypeEnum.MouseClick,
  MouseDoubleClick = MouseDoubleClickEventTypeEnum.MouseDoubleClick,
  MousePress = MousePressEventTypeEnum.MousePress,
  MouseRelease = MouseReleaseEventTypeEnum.MouseRelease,
  MouseScroll = MouseScrollEventTypeEnum.MouseScroll

}
