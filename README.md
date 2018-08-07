# Scatterbrain

Scatterbrain is intended to be a quick exploration tool for voxelwise regression, in the same way that [Scatterize](http://webtasks.keck.waisman.wisc.edu/scatterize/) is for spreadsheets.

You'll need:

* A 4D timeseries in .nii format, hopefully masked and compressed (but if not hey you'll have a huge slow file), size (i, j, k, *n*). Should be in MNI space.
* A spreadsheet with m columns (one per variable) and *n* rows. **n must be equal between the spreadsheet and the .nii file.**
* To specify the model. The voxel data will be your DV, spreadsheet values will be IVs.

You'll see:
* A statistical map of the ß of the coefficient of interest
* A scatterplot of the model at that voxel

It's being made at [Neurohackademy 2018](http://neurohackademy.org/neurohack_year/2018/).

# Thanks to:

* The organizers, instructors at Neurohackademy.
* The NIH and E-Science Institute for funding the event
* The authors of all of the libraries we're using. Of which there are many.