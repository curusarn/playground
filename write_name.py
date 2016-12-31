
import sys

print("Write your name.(with small letters)")


a = sys.stdin.readline()


if (a == "simon\n") or (a == "anna\n") or (a == "ondra\n") or (a == "martin\n"):
	print("Hi {0}".format(a))
else:
	print("FUCK YOU")
