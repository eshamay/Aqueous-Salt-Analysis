scp eric@cl7:/raid1/Analysis/Na2SO4+CTC/orderparams.coords.avg.dat Na2SO4+CTC.ordercoords.avg.dat
scp eric@cl7:/raid1/Analysis/NaNO3+CTC/orderparams.coords.avg.dat NaNO3+CTC.ordercoords.avg.dat
scp eric@cl7:/raid1/Analysis/NaCl+CTC/orderparams.coords.avg.dat NaCl+CTC.ordercoords.avg.dat
scp eric@cl7:/raid1/Analysis/H2O+CTC/orderparams.coords.avg.dat H2O+CTC.ordercoords.avg.dat
sed -i -e 's/^[ \t]*//g' *ordercoords.avg.dat
sed -i -e 's/[ \t]*$//g' *ordercoords.avg.dat
sed -i -e 's/positionUN/position	UN/g' *ordercoords.avg.dat
