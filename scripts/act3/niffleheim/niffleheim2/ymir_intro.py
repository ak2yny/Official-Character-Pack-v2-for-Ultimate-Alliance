# Generated by BehavEd
# ( "introduce ymir" )
setRecallActive("FALSE" )
metymir = getGameFlag("bosses", 21 )
if metymir == 0
     setGameFlag("bosses", 21, 1 )
     startCutScene("FALSE", "FALSE" )
     setEnable("ymir_magnet", "FALSE" )
     setEnable("ymir_magnet02", "FALSE" )
     setEnable("ymir_magnet03", "FALSE" )
     cameraSetClipPlane(8000.000 )
     cameraMove(" 8972.000 2677.000 436.000 ", 2.000 )
     cameraPan(" 0.000 -1.700 274.000 ", 2.000, "FALSE" )
     endCutScene("FALSE", "FALSE" )
     
     doomIsHere = isActorOnTeam("doomdlc" )
     if doomIsHere == 1
     	startConversation("act3/niffleheim/niffleheim2/3_niffleheim2_042_DLC" )
     else
     	startCharConversation("act3/niffleheim/niffleheim2/3_niffleheim2_040", "ICEMAN", "act3/niffleheim/niffleheim2/3_niffleheim2_042" )
     endif
endif

