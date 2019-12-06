# ob_utils
Python programs for analyzing onebreak results.

## Dependency

### sv_panel
Python (>= 2.7, >= 3.6)

### Software
[bedtools](http://bedtools.readthedocs.org/en/latest/)
tabix, bgzip

## Install

```
python setup.py install
```

## Commands

```
sv_panel merge_control [-h] result_list.txt merge_control.bedpe.gz
```
```
sv_panel convert_control [-h] merge_control.bedpe.gz result.txt
```

You can check the manual by typing
```
sv_panel merge_control -h
```
```
sv_panel convert_control -h
```
