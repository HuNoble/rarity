#!/usr/bin/env python

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


import csv
import os
import datetime

first_iteration_done = False

def convert_to_truefalse(y_or_n):
	if y_or_n.upper() == 'Y':
		return "True"
	else:
		return "False"

def add_new_row():
	path3 = os.getcwd()
	path3 = path3+"/"
	correct_input = False
	while not correct_input:
		try:
			datein = raw_input("Date: ")
			datetime.datetime.strptime(datein, '%Y/%m/%d')
			d = {"Date" : datein}
			correct_input = True
		except:
			print("You must provide a valid date in yyyy/mm/dd format!")
	correct_input = False
	
	while not correct_input:
		try:
			title = raw_input("Title: ")
			if not title:
				raise ValueError("Title can't be empty!")
			add_to_d = {"Title" : title}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			cweld = raw_input("Cweld: ")
			add_to_d = {"Cweld" : int(cweld)}
			d.update(add_to_d)
			correct_input = True
		except:
			print("Cweld must be an integer!")
	correct_input = False
	
	while not correct_input:
		try:
			url = raw_input("Url: ")
			if not url:
				raise ValueError("Url can't be empty!")
			add_to_d = {"Url" : url}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			severity = raw_input("Severity: ")
			if severity.upper() == 'INFO':
				severity = 'Info'
			elif severity.upper() == 'LOW':
				severity = "Low"
			elif severity.upper() == 'MEDIUM':
				severity = "Medium"
			elif severity.upper() == 'HIGH':
				severity = "High"
			elif severity.upper() == 'CRITICAL':
				severity = "Critical"
			else:
				raise ValueError('Severity must be Info, Low, Medium, High or Critical!')
			add_to_d = {"Severity" : severity}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			description = raw_input("Description: ")
			if not description:
				raise ValueError("Description can't be empty!")
			add_to_d = {"Description" : description}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			mitigation = raw_input("Mitigation: ")
			if not mitigation:
				raise ValueError("Mitigation can't be empty!")
			add_to_d = {"Mitigation" : mitigation}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			impact = raw_input("Impact: ")
			if not impact:
				raise ValueError("Impact can't be empty!")
			add_to_d = {"Impact" : impact}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			references = raw_input("References: ")
			if not references:
				raise ValueError("References can't be empty!")
			add_to_d = {"References" : references}
			d.update(add_to_d)
			correct_input = True
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			active = raw_input("Active (y/n): ")
			if (active.upper() == 'Y') | (active.upper() == 'N'):
				active = convert_to_truefalse(active)
				add_to_d = {"Active" : active}
				d.update(add_to_d)
				correct_input = True
			else:
				raise ValueError('Input must be y or n!')
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			verified = raw_input("Verified (y/n): ")
			if (verified.upper() == 'Y') | (verified.upper() == 'N'):
				verified = convert_to_truefalse(verified)
				add_to_d = {"Verified" : verified}
				d.update(add_to_d)
				correct_input = True
			else:
				raise ValueError('Verified must be y or n!')
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			falsepositive = raw_input("FalsePositive (y/n): ")
			if (falsepositive.upper() == 'Y') | (falsepositive.upper() == 'N'):
				falsepositive = convert_to_truefalse(falsepositive)
				add_to_d = {"FalsePositive" : falsepositive}
				d.update(add_to_d)
				correct_input = True
			else:
				raise ValueError('FalsePositive must be y or n!')
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	while not correct_input:
		try:
			duplicate = raw_input("Duplicate (y/n): ")
			if (duplicate.upper() == 'Y') | (duplicate.upper() == 'N'):
				duplicate = convert_to_truefalse(duplicate)
				add_to_d = {"Duplicate" : duplicate}
				d.update(add_to_d)
				correct_input = True
			else:
				raise ValueError('Duplicate must be y or n!')
		except ValueError as err:
			print(err.args)
	correct_input = False
	
	print(d)
	
	global first_iteration_done
	if not first_iteration_done:
		with open(path3 + 'extend.csv', 'w') as fw:
			writer = csv.writer(fw, delimiter=',')
			writer.writerow(d.keys())
	first_iteration_done = True
	
	good_input = raw_input("Is the given information correct? (y/n)")
	if good_input.upper() == 'Y':
		with open(path3 + 'extend.csv', 'a') as fw:
			writer = csv.writer(fw, delimiter=',')
			writer.writerow(d.values())
			print("Row saved.")
	else:
		print("Row discarded.")
	
def main():
	print("Welcome to Rarity - 'cause who the hell writes reports in the age of automation?")
	print('\n')
	newone = True
	while newone:
		add_new_row()
		some_random_shit_user_wrote = raw_input("Do you want to add another row? (y/n)")
		if not some_random_shit_user_wrote.upper() == 'Y':
			newone = False
	

if __name__ == "__main__":
	main()
