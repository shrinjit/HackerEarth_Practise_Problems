import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
ap.add_argument( "--name_of_other_person", required=True,
	help="name of the user")
args = vars(ap.parse_args())
# display a friendly message to the user
print('these are the arguments ',args)
print("Hi there {}, it's nice to meet you! and I am {}".format(args["name"],args["name_of_other_person"]))