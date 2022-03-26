
We uploded 2 versions because of cv2 version bug: the erode do dilate and dilate do erode. (it dependes on the cv2 version that you got).

main_v1.py:
	
	this is the version with the bug,
	
	1) do cv2.dilate
	2) do cv2.erode

main_v2.py:

	in this version we switched between the functions so:

	1) do cv2.erode
	2) do cv2.dilate


to run the program, run in the terminal the python project with the image argumant, exmple:

	>python main_v1.py text.png


Niv Zetuni 307852897
Gil Yadgar 311334825

