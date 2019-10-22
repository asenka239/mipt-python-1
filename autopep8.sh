for i in $(find . -name "*.py"); do
	echo $i;
	autopep8 --in-place --aggressive --aggressive $i;
done