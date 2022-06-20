#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
from os.path import expanduser, realpath, split, join, exists
from os import rename


def main(args):
	flags = 0 if args.case_sensitive else re.I
	file_num = 0
	for f in args.files:
		dir_name, file_name = split(realpath(expanduser(f)))
		new_file_name = None
		try:
			new_file_name = re.sub(args.exp, args.repl, file_name, 0, flags)
		except re.error as e:
			print("ERROR:", e)
			exit(1)

		if file_name == new_file_name:
			continue

		new_full_path = join(dir_name, new_file_name)
		if exists(new_full_path):
			print(f"ERROR: target file '{new_file_name}' already exists")
			exit(1)

		if args.verbose:
			print(f"'{file_name}'", "→", f"'{new_file_name}'")

		if not args.dry_run:
			rename(f, new_full_path)
			file_num += 1

	if file_num == 1:
		print(f"{file_num} file renamed.")
	else:
		print(f"{file_num} files renamed.")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="rename files with regular expressions")
	parser.add_argument("exp", metavar="expression", type=str, help="regex search expression")
	parser.add_argument("repl", metavar="replacement", type=str, help="regex replacement expression")
	parser.add_argument("files", metavar="file", type=str, nargs="+", help="the files to operate on")

	parser.add_argument("-v", "--verbose", action="store_true", help="explain actions before doing them")
	parser.add_argument("-n", "--dry-run", action="store_true", help="don't modify any files")
	parser.add_argument("-s", "--case-sensitive", action="store_true", help="disable case-insensitive mode")

	args = parser.parse_args()
	main(args)
