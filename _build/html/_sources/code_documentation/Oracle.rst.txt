
Code docs -- *oracle_final.cpp*
=================================


How to receive a hint
----------------------

the robot goes around in search of a ArUco code containing the ID of the hint. When it finds one hint, it makes a service request to the Oracle declaring the found hint. This request is of type *erl3/Marker*, made as follows:

.. code-block::
	
	int32 markerId
	---
	erl3/ErlOracle oracle_hint

the field of type *erl3/ErlOracle* has these fields:

.. code-block::
	
	int32 ID
	string key
	string value


How to check if the hint is valid
----------------------------------

to check whether a specific ID is the solution of the mystery, call the service */oracle_solution* of type ``erl2/Oracle``. Here's the prototype of the service:

.. code-block::
	
	---
	int32 ID


Hints generation
-----------------

referring to the code, 

* the ID of the hint is from 0 to 5
* the orale knows only the IDs and not the corresponding solution in terms of where, what and who

in particular,

* the *winID* is, randomly choosen from 0 to 5
* the array *uIDs* contains the inconsistent IDs
