#!/usr/bin/env python

# -*- coding: utf-8 -*-
'''
MLEPJSON Read json file with inputs and outputs. Need to extract the order for both 

 (C) 2017 by Willy Bernal (Willy.BernalHeredia@nrel.gov)
'''
import json
import mlep

def mlepJSON (filename):

	fid = open(filename,"r")
	json_string = fid.read()
	parsed_json = json.loads(json_string)

	# Initialize Variables
	inputs_num = 0
	outputs_num = 0
	inputs_list = list()
	outputs_list = list()

	# Loop
	for i in range(0,len(parsed_json)):
		if parsed_json[i]['source'] == 'EnergyPlus':
			inputs_dict = {key: parsed_json[i][key] for key in ('type','name','id')}
			inputs_list.append(inputs_dict['id'].replace('r:',''))
			inputs_num += 1
		elif parsed_json[i]['source'] == 'Ptolemy':
			outputs_dict = {key: parsed_json[i][key] for key in ('variable','id')}
			outputs_list.append(outputs_dict['id'].replace('r:',''))
			outputs_num += 1

	return[inputs_list,outputs_list]