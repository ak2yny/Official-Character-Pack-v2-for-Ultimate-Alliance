# Generated by BehavEd
# ( "has blade already been unlocked?" )
check_blade = getGameFlag("murder4", 1 )
if check_blade == 0
     # ( "blade has not already been unlocked--spawn and unlock him" )
     remove ( "trigger_claw", "trigger_claw" )
     act("blade_trapped", "blade_trapped" )
     waittimed ( 4.000 )
     setSegmentVisible("bladeunlock", "0101_sword_segment", "0")
     setSegmentVisible("bladeunlock", "0101_gun_segment", "0")
     cameraReset( )
     unlockCharacter("blade", "" )
     setGameFlag("murder4", 1, 1 )
     remove ( "action_figure_blade", "action_figure_blade" )
     setHintType("bladeunlock", "importanttalk" )
endif
setInvulnerable("_ACTIVATOR_", "FALSE" )
