#!/bin/bash
 
## Part 1:  Set up python
PYPY_VERSION=2.4.0
HOME=/home/core
mkdir -p $HOME
cd $HOME
block-until-url https://bitbucket.org/pypy/pypy/downloads/pypy-$PYPY_VERSION-linux64.tar.bz2
#
wget -O - https://bitbucket.org/pypy/pypy/downloads/pypy-$PYPY_VERSION-linux64.tar.bz2 |tar -xjf -
mv -n pypy-$PYPY_VERSION-linux64 pypy
#
## library fixup
mkdir -p pypy/lib
ln -snf /lib64/libncurses.so.5.9 $HOME/pypy/lib/libtinfo.so.5
 
mkdir -p $HOME/bin
#
cat > $HOME/bin/python <<EOF
#!/bin/bash
LD_LIBRARY_PATH=$HOME/pypy/lib:$LD_LIBRARY_PATH exec $HOME/pypy/bin/pypy "\$@"
EOF
#
chmod +x $HOME/bin/python
$HOME/bin/python --version
