# Generated by BehavEd
setRecallActive("TRUE" )
cameraFade(0.000, 1.000 )
cameraSetClipPlane(20000.000 )
first_visit = getGameFlag("Heli1", 1 )
defeated_scorpion = getGameFlag("Heli1", 2 )
if first_visit == 0
     startCutScene("FALSE", "FALSE" )
     setGameFlag("Heli1", 1, 1 )
     cameraFollowMotionPath("heli_carrier/opening_cam", "mp_opening_cam", "TRUE", "TRUE", "FALSE", "" )
     act("intro_relay03", "intro_relay03" )
     waittimed ( 0.250 )
     endCutScene("FALSE", "TRUE" )
     remove ( "intro_ultron01", "intro_ultron01" )
     remove ( "intro_ultron02", "intro_ultron02" )
     waittimed ( 0.250 )
     objective ( "Heli_Obj0",  "EOBJCMD_SHOW" )
     objective ( "Heli_Obj10",  "EOBJCMD_SHOW" )
endif
if defeated_scorpion == 1
     remove ( "scorpion_fight_trig", "scorpion_fight_trig" )
     remove ( "scorpion_spawner", "scorpion_spawner" )
     remove ( "ultrona", "ultrona" )
     remove ( "ultronb", "ultronb" )
     remove ( "ultronc", "ultronc" )
     remove ( "ultrond", "ultrond" )
     setEnable("link_heli2", "TRUE" )
endif

