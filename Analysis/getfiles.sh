scp eric@cl7:/raid1/Analysis/Na2SO4+CTC/orderparams.coords.avg.100+.dat Na2SO4+CTC.ordercoords.avg.dat
scp eric@cl7:/raid1/Analysis/NaNO3+CTC/orderparams.coords.avg.100+.dat NaNO3+CTC.ordercoords.avg.dat
sed -i -e 's/^[ \t]*//g' *ordercoords.avg.dat
sed -i -e 's/[ \t]*$//g' *ordercoords.avg.dat
sed -i -e 's/positionUN/position	UN/g' *ordercoords.avg.dat

scp eric@cl7:/raid1/Analysis/Na2SO4+CTC/density.avg.100+.dat Na2SO4+CTC.density.avg.dat
scp eric@cl7:/raid1/Analysis/NaNO3+CTC/density.avg.100+.dat NaNO3+CTC.density.avg.dat

scp eric@cl7:/raid1/Analysis/NaNO3+CTC/coordination.avg.100+.dat NaNO3+CTC.coordination.avg.dat
scp eric@cl7:/raid1/Analysis/Na2SO4+CTC/coordination.avg.100+.dat Na2SO4+CTC.coordination.avg.dat

scp eric@cl7:/raid1/Analysis/Na2SO4+CTC/orderparams.avg.100+.dat Na2SO4+CTC.orderparams.avg.dat
scp eric@cl7:/raid1/Analysis/NaNO3+CTC/orderparams.avg.100+.dat NaNO3+CTC.orderparams.avg.dat
