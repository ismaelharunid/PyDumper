# PyDumper

A python object dumper.

The purpose of this module is to create a configurable and easy to implement object/value dumper.

Key features:
* can fall back to repr (object.__repr__) methods
* formating can be customized based of it's reference from the parent (if there is one) by the key, index or attribute name.
* formatting can be customized based on it's type or instantiation.
* formatting can be customized based on complex hierchy rules and criteria.
* supports pretty printing.
* supports stream output for dumping.
* supports short, long, multiline, and verbose formatting.
* makes you happy when your feeling low.

This is similar to various stringifying and json type libraries except that PyDump makes noo assumptions about the expectations other then to fall back to native python repr formatting when no logic is provided.

Some examples include: a configuration dumper, a json dumper, a PyWavefront dumper that makes it much easier to scan your object files,, and finially a PyWaavefront .obj format dumper for the purposes of cleaning existing .onj files or to create ,obj files from python data.

Currently, as this is a brand spanking new project, not all the code is uploaded.  And the project is not even alpha yet.  But I have already created this once before and although I am rewriting it, it's going pretty fast.  God willing, it will be all up within the next week.

I hope you find it useful and don't hestitate to ask for things like documentation or support.  And if you appreciate this project please send money, or praise is also ok.





