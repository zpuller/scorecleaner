rm -rf tmp/ outputs/
mkdir tmp/ outputs/
python3 py/split_pdf.py inputs/etudes.pdf tmp
ls tmp | xargs -I{} qlmanage -t -s 1600 -o tmp tmp/{} 2>&1 > /dev/null
ls tmp | grep png | xargs -I{} python3 py/gray.py tmp/{} tmp/gray_{}
ls tmp | grep gray | grep png$ | xargs -I{} sips -s format pdf tmp/{} --out tmp/{}.pdf 2>&1 > /dev/null
ls tmp | grep pdf.png.pdf | xargs -I{} echo tmp/{} | xargs python3 py/cat_pdfs.py outputs/etudes.pdf
rm -rf tmp/
