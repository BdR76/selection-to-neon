selection to neon glow
======================

This is a GIMP Python plug-in to create neon glow effect based on a selection.
Turn selected region into lightsaber or 80s cartoon underlighting (aka "Bipack
Glow") effects.

![Selection to neon glow effect](/preview.png?raw=true "preview")

How to use it
-------------
Download and install [GIMP](https://www.gimp.org/) and copy the file
`selection_neon_glow.py` into the following directory:

	.\GIMP 2\lib\gimp\2.0\plug-ins\

After you've put the file in the plug-ins directory, open GIMP and there
should be a new menu item available, under `Script-Fu -> Selection to neon glow`.

Known bugs / trouble shooting
-----------------------------
There is a bug in GIMP for Windows 64bit causing an error when selecting a color
from the plug-in dialog. When clicking on the color widget will give an eror message
"unable to run GimpPdbProgress callback", this bug [has been reported](https://bugzilla.gnome.org/show_bug.cgi?id=795999).

When merging the new layers into a single layer, it somehow looks less "glowy".
Don't know what causes this, possibly a bug in GIMP, if anyone knows why please let me know.

Questions, comments -- Bas de Reuver (bdr1976@gmail.com)
