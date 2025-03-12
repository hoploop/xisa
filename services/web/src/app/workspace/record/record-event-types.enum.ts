import { KeyComboPressEventTypeEnum, MouseClickRightEventTypeEnum, MousePressRightEventTypeEnum } from "@api/index";
import { KeyPressEventTypeEnum } from '@api/model/key-press-event';
import { KeyReleaseEventTypeEnum } from '@api/model/key-release-event';
import { MouseClickLeftEventTypeEnum } from '@api/model/mouse-click-left-event';
import { MousePressLeftEventTypeEnum } from '@api/model/mouse-press-left-event';
import { MousePressMiddleEventTypeEnum } from '@api/model/mouse-press-middle-event';
import { MouseReleaseLeftEventTypeEnum } from '@api/model/mouse-release-left-event';
import { MouseReleaseRightEventTypeEnum } from '@api/model/mouse-release-right-event';
import { MouseReleaseMiddleEventTypeEnum } from '@api/model/mouse-release-middle-event';
import { MouseScrollEventTypeEnum } from '@api/model/mouse-scroll-event';

export enum RecordEventTypes {
  KeyComboPress = KeyComboPressEventTypeEnum.KeyComboPress,
  KeyPress = KeyPressEventTypeEnum.KeyPress,
  KeyRelease = KeyReleaseEventTypeEnum.KeyRelease,
  MouseClickLeft = MouseClickLeftEventTypeEnum.MouseClickLeft,
  MouseClickRight =MouseClickRightEventTypeEnum.MouseClickRight,
  MousePressLeft = MousePressLeftEventTypeEnum.MousePressLeft,
  MousePressMiddle = MousePressMiddleEventTypeEnum.MousePressMiddle,
  MousePressRight = MousePressRightEventTypeEnum.MousePressRight,
  MouseReleaseLeft = MouseReleaseLeftEventTypeEnum.MouseReleaseLeft,
  MouseReleaseRight = MouseReleaseRightEventTypeEnum.MouseReleaseRight,
  MouseReleaseMiddle = MouseReleaseMiddleEventTypeEnum.MouseReleaseMiddle,
  MouseScroll = MouseScrollEventTypeEnum.MouseScroll

}
