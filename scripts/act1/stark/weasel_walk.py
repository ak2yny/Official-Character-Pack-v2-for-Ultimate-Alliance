# Generated by BehavEd
# ( "This puts Weasel on his path to get out of the way." )
lockControls(0.500 )
cameraFade(1.000, 0.250 )
waittimed ( 0.250 )
cameraMove(" 63.000 586.000 269.000 ", 0.000 )
cameraPan(" 0.000 32.000 90.000 ", 0.000, "FALSE" )
# ( "***********Has the player talked to Weasel***********" )
# ( "The sequence should go weasel->vision->black widow->fury" )
# ( "conv_vars 3 = unlock Fury line" )
# ( "conv_vars 10 = unlock vision line" )
setGameFlag("conv_vars", 10, 1 )
objective ( "stark_obj10",  "EOBJCMD_SHOW" )
# ( "***********END Has the player talked to Weasel***********" )
waittimed ( 0.300 )
setEnable("jarvis", "TRUE" )
copyOriginAndAngles("weasel", "wp_weaselwalk02" )
copyOriginAndAngles("jarvis", "wp_jarvis_stand01" )
waittimed ( 0.100 )
setWaypointPath("weasel", "weaselpath", 1 )
copyOriginAndAngles("_HERO1_", "hero_spot05" )
copyOriginAndAngles("_HERO2_", "hero_spot06" )
copyOriginAndAngles("_HERO3_", "hero_spot07" )
copyOriginAndAngles("_HERO4_", "hero_spot08" )
setEnable("trigger_zonelink01", "TRUE" )
waittimed ( 0.100 )
cameraFade(0.000, 0.250 )
cameraResetOldSchool( )
