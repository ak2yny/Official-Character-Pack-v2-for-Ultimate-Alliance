# Generated by BehavEd
# ( "introduce ultimo in a cut scene; start conversation" )
act("s_ultimo", "s_ultimo" )
startCutScene("FALSE", "FALSE" )
cameraFocusToEntity("cam_ultimo", 512.000, 45.000, 0.000, 1.000 )
waittimed ( 1.000 )
# ( "PERSISTENCE--indicate ultimo has been introduced" )
setGameFlag("mandarin3", 1, 1 )
startCharConversation("act1/mandarin/mandarin3/1_mandarin3_010", "Hulk", "act1/mandarin/mandarin3/1_mandarin3_020" )
setEnable("trig_ultimo_arena", "TRUE" )

