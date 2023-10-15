version=$1
mkdir -p build/areace
cp -r resources addon.xml LICENSE.txt script.py build/areace
cd build && zip -rm areace-$version.zip areace