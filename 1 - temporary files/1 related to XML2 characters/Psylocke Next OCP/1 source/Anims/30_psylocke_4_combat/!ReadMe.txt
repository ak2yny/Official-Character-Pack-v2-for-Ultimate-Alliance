Animation Creation Tool for MUA V2 by Vicarious Visions, defogexa, nikita488 and ak2yny
----------------------------------

What is it for:
Characters are limited to use animations present in animation sets. To add more variety and to be able to add custom animations (as exported with Alchemy exporter in 3dsMax), we are required to combine multiple individual animations (exported as igb files) into single animation sets ([##]_[charactername][_4_combat].igb) which include animation names supported by the "shared_anims" database (228 animation names). We can use each animation available from many different versions, including XML2 PC, and MUA/MUA2 Wii. To access those individual animations, we have to extract them from the animation sets (eg. 03_wolverine.igb, or fightstyle_finesse1.igb).
What's an animation set: basically any .igb file from the "actors" folder, whose filename doesn't consist of numbers only.


To Extract:

  1 Copy the animation set you want to pull from into the same folder as "_extract.bat" and "_animations.txt".
  2 Run the "_extract.bat" file.
    Information: The batch creates sub-folders and extract lists for all igb's in the folder.
                 The extracted animation files (*.igb) can be found in each sub-folder (named after the animation set).
    If any extract-[...].txt or "extract.txt" exist, you can press "Y" to use them.
  1 Alternatively, instead of copying animation sets, drag & drop them onto the "_extract.bat" file.
  1 Alternatively, drag & drop one or multiple folders onto the "_extract.bat" file for batch processing.
    


To Combine:

  1 Copy the individual animation files you want into a folder with "_fightstyle_default" and "_combine.bat",
    or copy "_fightstyle_default" and "_combine.bat" into the folder where your individual animation files are.
  2 Rename the igb's as the animations you want them to be recognized as.
     (When you rename, be sure it's accounted for in the data\shared_anims.engb*. For example, by default there's no power_5_loop.)
  3 Run the "_combine.bat" file and enter the name of the your custom animation set.
 (4)Open the custom animation set in a hex editor, go to offset 2C, change 09 to 08 and save.**
  3 Alternatively, instead of copying individual animation files, drag & drop them onto the "_combine.bat" file.
  3 Alternatively, drag & drop one or multiple folders onto the "_extract.bat" file for batch processing.



*  The names can also be found in "_animations.txt" under ---shared_anims---.
** It's recommended to use the version hack by nikita488 (version number changed in libIGCore.dll) instead.