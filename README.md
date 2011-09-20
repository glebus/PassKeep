About
-----

Console slim program for generate unique password's for sites.

Example usage
-------------

	$~/Development/PassKeep>./PassKeep.py
	Enter passphrase:
	Enter site domain (like www.example.com): www.exampler.com
	Password from site 'www.exampler.com' is: 3675ac5c859c806

How use as module
-----------------

1. Import class `PassKeep`

		from PassKeep import PassKeep

2. Create object

		p = PassKeep()

3. Set passphrase and site domain

		p.site = "www.example.com"
		p.passphrase = "mybigpass"

4. Bee happy :)

		print p

Alternative info
----------------

		>>> from PassKeep import PassKeep
		>>> help(PassKeep)

