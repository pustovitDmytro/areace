version=$1
# mkdir -p build/script.areace
cp addon.xml build/script.areace
cd build && zip -rm areace-$version.zip script.areace