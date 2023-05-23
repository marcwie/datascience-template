to_execute=(
    'NAME_OF_FIRST_NOTEBOOK'
    'NAME_OF_SECOND_NOTEBOOK'
)

cd notebooks

for filename in ${to_execute[@]}
do
	echo $filename
	poetry run jupyter nbconvert --to=python --output=out $filename
	poetry run python out.py
done

rm out.py
