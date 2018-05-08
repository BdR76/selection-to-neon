#!/usr/bin/env python

# Selection to neon glow effect

# based in part on Glow Rel 1 by Tin Tran (http://bakon.ca/gimplearn)

from gimpfu import *

def python_neonglow_test(image, layer, glowcolor, glowsize):

	# prepare for clean up later
	prev_layer = image.active_layer
	pdb.gimp_image_undo_group_start(image)
	pdb.gimp_context_push()
	
	# gaussian blur sizes (example 45px, 30px 15px)
	glowsize2 = (glowsize * 2) / 3
	glowsize3 = glowsize / 3
	grow = glowsize / 15

	pdb.gimp_context_set_default_colors()

	# check if there is any selection
	is_selection, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
	
	if not (is_selection):
		pdb.gimp_message('There is nothing selected, create a selected region and try again.')
	else:
		# copy selection to new layer
		pdb.gimp_edit_copy(image.active_layer)
		glowarea = pdb.gimp_edit_paste(layer, False)
		pdb.gimp_floating_sel_to_layer(glowarea)
		# pdb.plug_in_autocrop_layer(image, image.active_layer)

		# fill new selection with pure white color
		pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.active_layer)
		pdb.gimp_context_set_foreground((255,255,255)) # white color
		pdb.gimp_edit_fill(glowarea,FOREGROUND_FILL)
		image.active_layer.name = "Glow highlight area"

		# adds small outerglow layer
		glowlayer1 = pdb.gimp_layer_new(image,image.width,image.height,RGBA_IMAGE,"outer glow",100,NORMAL_MODE)
		pdb.gimp_image_insert_layer(image,glowlayer1,None,1)
		pdb.gimp_selection_grow(image,grow)
		pdb.gimp_context_set_foreground(glowcolor)
		pdb.gimp_edit_fill(glowlayer1,FOREGROUND_FILL)
		pdb.gimp_selection_none(image)
		pdb.plug_in_gauss(image,glowlayer1,glowsize,glowsize,1)
		image.active_layer.name = "Outer glow 1"
		
		#dodge outerglow copy
		glowlayer2 = pdb.gimp_layer_new_from_drawable(glowlayer1,image)
		pdb.gimp_image_insert_layer(image,glowlayer2,None,0)
		pdb.plug_in_gauss(image,glowlayer2,glowsize2,glowsize2,1)
		pdb.gimp_layer_set_mode(glowlayer2,DODGE_MODE)
		image.active_layer.name = "Outer glow 2"

		glowlayer3 = pdb.gimp_layer_new_from_drawable(glowlayer2,image)
		pdb.gimp_image_insert_layer(image,glowlayer3,None,1)
		pdb.plug_in_gauss(image,glowlayer3,glowsize3,glowsize3,1)
		pdb.gimp_layer_set_mode(glowlayer3,DODGE_MODE)
		image.active_layer.name = "Outer glow 3"

		# merging the new layers somehow makes it less "glowy" (why?)
		# make only new layers visible
		# for checklayer in image.layers:
		# 	# check if layer is a group
		# 	checklayer.visible = ((checklayer == glowarea) or (checklayer == glowlayer1) or (checklayer == glowlayer2) or (checklayer == glowlayer3))
		# 		
		# # merge layers
		# image.active_layer = glowarea
		# pdb.gimp_image_merge_visible_layers(image, 0)

	# do clean up
	pdb.gimp_context_pop()
	image.active_layer = prev_layer
	image.active_layer.visible = True
	pdb.gimp_image_undo_group_end(image)
	# pdb.gimp_displays_flush()

register(
	"python_fu_selection_to_neon_glow",
	"Selection to neon glow effect",
	"Selection to neon glow effect",
	"BdR",
	"BdR",
	"May 2018",
	"<Image>/Python-Fu/Selection to neon glow",             #Menu path
	"RGB*, GRAY*", 
	[
		(PF_COLOR, "glowcolor",  "Glow color:",  (0,128,255)),
		(PF_INT, "glowsize", "Size of glow:", 45)
	],
	[],
	python_neonglow_test)

main()
