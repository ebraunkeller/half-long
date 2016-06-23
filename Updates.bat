setlocal
cd "c:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat"
set SAVESTAMP=%DATE:/=-%@%TIME::=-%
set SAVESTAMP=%SAVESTAMP: =%
echo ... > DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 %SAVESTAMP%
echo ... >> DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 Copyright (c) 2015 BKLSchoolVision Data Refresh for %SAVESTAMP%

cd "c:\Users\Elaine\Documents\BKL\Danvers\Scripts
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDownload.py"

cd "c:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat"
echo ...  Download from Google drive complete>> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 
echo ...  Begin updating Great Oak >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 

del GoGr1.csv, GoGr1_2016.csv, GODemo.csv,GOGrK.csv
del GoGr2.csv, GoGr2_2016.csv, 
del GoGr3.csv, GoGr3_2016.csv
del GoGr4.csv, GoGr4_2016.csv
del GoGr5.csv, GoGr5_2016.csv
del DISGr1.csv,DISGr2.csv,DISGr3.csv,DISGr4.csv,DISGrK.csv,DistrictDemo.csv
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGrK.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO Kindergarten Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGrK.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr1.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO First Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGr1_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr2.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO Second Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGr2_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr3.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO Third Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGr3_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr4.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO Fourth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGr4_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr5.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\GO\GO Fifth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\GoGr5_2016.csv"
type GoGr1_2016.csv,GoGr1_2015.csv> GoGr1.csv
type GoGr2_2016.csv,GoGr2_2015.csv> GoGr2.csv
type GoGr3_2016.csv,GoGr3_2015.csv> GoGr3.csv
type GoGr4_2016.csv,GoGr4_2015.csv> GoGr4.csv
type GoGr5_2016.csv,GoGr5_2015.csv> GoGr5.csv
echo ...  Great Oak Completed...begin updating Highlands >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 

del HLGr1.csv, HLGr1_2016.csv, HLDemo.csv, HLGrK.csv
del HLGr2.csv, HLGr2_2016.csv
del HLGr3.csv, HLGr3_2016.csv
del HLGr4.csv, HLGr4_2016.csv
del HLGr5.csv, HLGr5_2016.csv
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGrK.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands Kindergarten Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGrK.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr1.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands First Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGr1_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr2.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands Second Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGr2_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr3.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands Third Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGr3_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr4.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands Fourth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGr4_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr5.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\HL\Highlands Fifth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\HLGr5_2016.csv"
type HLGr1_2016.csv,HLGr1_2015.csv> HLGr1.csv
type HLGr2_2016.csv,HLGr2_2015.csv> HLGr2.csv
type HLGr3_2016.csv,HLGr3_2015.csv> HLGr3.csv
type HLGr4_2016.csv,HLGr4_2015.csv> HLGr4.csv
type HLGr5_2016.csv,HLGr5_2015.csv> HLGr5.csv
echo ...  Highlands completed...begin updating Smith >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 

del SMGr1.csv, SMGr1_2016.csv, SMDemo.csv, SMGrK.csv
del SMGr2.csv, SMGr2_2016.csv
del SMGr3.csv, SMGr3_2016.csv
del SMGr4.csv, SMGr4_2016.csv
del SMGr5.csv, SMGr5_2016.csv
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGrK.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith Kindergarten Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGrK.csv"

python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr1.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith First Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGr1_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr2.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith Second Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGr2_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr3.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith Third Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGr3_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr4.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith Fourth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGr4_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr5.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\SM\Smith Fifth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\SMGr5_2016.csv"
type SMGr1_2016.csv,SMGr1_2015.csv> SMGr1.csv
type SMGr2_2016.csv,SMGr2_2015.csv> SMGr2.csv
type SMGr3_2016.csv,SMGr3_2015.csv> SMGr3.csv
type SMGr4_2016.csv,SMGr4_2015.csv> SMGr4.csv
type SMGr5_2016.csv,SMGr5_2015.csv> SMGr5.csv
echo ...  Smith completed...begin updating Riverside >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1

del RSGr1.csv, RSGr1_2016.csv, RSDemo.csv,RSGrK.csv
del RSGr2.csv, RSGr2_2016.csv
del RSGr3.csv, RSGr3_2016.csv
del RSGr4.csv, RSGr4_2016.csv
del RSGr5.csv, RSGr5_2016.csv
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGrK.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside Kindergarten Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGrK.csv"

python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr1.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside First Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGr1_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr2.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside Second Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGr2_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr3.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside Third Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGr3_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr4.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside Fourth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGr4_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr5.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\RS\Riverside Fifth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\RSGr5_2016.csv"
type RSGr1_2016.csv,RSGr1_2015.csv> RSGr1.csv
type RSGr2_2016.csv,RSGr2_2015.csv> RSGr2.csv
type RSGr3_2016.csv,RSGr3_2015.csv> RSGr3.csv
type RSGr4_2016.csv,RSGr4_2015.csv> RSGr4.csv
type RSGr5_2016.csv,RSGr5_2015.csv> RSGr5.csv
echo ...  Riverside completed...begin updating Thorpe >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 

del THGr1.csv, THGr1_2016.csv, THDemo.csv, THGrK.csv
del THGr2.csv, THGr2_2016.csv
del THGr3.csv, THGr3_2016.csv
del THGr4.csv, THGr4_2016.csv
del THGr5.csv, THGr5_2016.csv
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGrK.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe Kindergarten Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGrK.csv"

python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr1.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe First Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGr1_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr2.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe Second Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGr2_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr3.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe Third Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGr3_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr4.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe Fourth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGr4_2016.csv"
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\UpdateDanversGr5.py"  "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\TH\Thorpe Fifth Grade Reading Data SY15-16.csv" "C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\THGr5_2016.csv"
type THGr1_2016.csv,THGr1_2015.csv> THGr1.csv
type THGr2_2016.csv,THGr2_2015.csv> THGr2.csv
type THGr3_2016.csv,THGr3_2015.csv> THGr3.csv
type THGr4_2016.csv,THGr4_2015.csv> THGr4.csv
type THGr5_2016.csv,THGr5_2015.csv> THGr5.csv

python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\StudentDemo.py" "C:\Users\Elaine\Documents\BKL\Danvers\RawData15-16\Demographics.csv" C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\
echo ...  Thorpe completed. Creating District files >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 
python "C:\Users\Elaine\Documents\BKL\Danvers\Scripts\CreateDistrictFiles.py"

echo ...  Update complete >> c:\Users\Elaine\Documents\BKL\Danvers\Scripts\DanversDataUpdateLog_%SAVESTAMP%.txt 2>&1 