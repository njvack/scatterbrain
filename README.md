## scatterbrain

Scatterbrain aims to be a spiritual child of [scatterize](http://webtasks.keck.waisman.wisc.edu/scatterize/d/Acdck0qHJo#h=2&m=OLS&x=1&y=6) and [NeuroSynth](http://neurosynth.org/). It'll allow researchers to upload the results of an analysis (done in an existig package), the data that went into the analysis, and a file describing what analyses were done.

Then, researchers can click around the brain, viewing scatterplots (at any voxel, and easily see outliers or such.

## Inputs

Ultimately, everything is going to get packaged up in a .zip file and digestified by an importer.

### Raw data

The data that went into a given set of analyses will be split into two parts:

1: a CSV containing columns for:

* An ID (for example, participant ID number)
* One or more voxelwise variables (filenames, pointing to niftis)
* One oe more volumewise variables (scalar numbers)
* Zero or more "annotation" columns containing free text.

Missing data is OK.

So an example might look like:

<table>
<tr><td>id<td></td>understood<td></td>age<td></td>awesomeness<td></td>activation</td></tr>
<tr><td>964<td></td>1<td></td>19<td></td>0.15939<td></td>964/betas.nii</td></tr>
<tr><td>965<td></td>1<td></td>24<td></td>0.017494<td></td>965/betas.nii</td></tr>
<tr><td>966<td></td>0<td></td>21<td></td>3<td></td>966/betas.nii</td></tr>
<tr><td>967<td></td>1<td></td>42<td></td>0.61647<td></td>967/betas.nii</td></tr>
<tr><td>968<td></td>1<td></td>30<td></td>0.66278<td></td>968/betas.nii</td></tr>
<tr><td>969<td></td>1<td></td>22<td></td>0.67336<td></td>969/betas.nii</td></tr>
<tr><td>970<td></td>1<td></td>21<td></td>0.52115<td></td>970/betas.nii</td></tr>
</table>

If you have multi-volume nifti files and want to refer to volume numbers, use a slash: for example `betas.nii/0` for the first volume or `contrast.nii/10` for the eleventh.

2: The actial nifti files. As long as the path in the file columns get you there, you're good.

### Analysis Descriptions

Another CSV file, this one containing:

* An analysis description
* (Optional) the software package that did the analysis
* A filename for a statistical map
* A model descripiton 

OK, but this is getting out of scope at the moment. More later.

