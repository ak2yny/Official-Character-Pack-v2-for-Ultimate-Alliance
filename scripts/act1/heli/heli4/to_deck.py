# Generated by BehavEd
# ( "go up to the deck" )
setAmbientLightColor(" 0.000 0.250 0.500 ", 1.000 )
cameraSetClipPlane(30000.000 )
cameraFreeFOV(70.000 )
beat_fff = getGameFlag("bosses", 2 )
if beat_fff == 0
     setRecallActive("FALSE" )
     setAIActive("finfangfoom", "TRUE" )
     setInvulnerable("finfangfoom", "FALSE" )
     setMusicOverride("music/heli4_x", 1.000 )
     setZoneVar("heroondeck", 1 )
     # ( "turn gunships back on" )
     met_fff = getGameFlag("bosses", 1 )
     if met_fff == 1
          setEnable("gunship_control", "TRUE" )
          act("gunship_control", "gunship_control" )
     endif
endif

