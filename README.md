# suppression-test-python-multi-operation

This repository is used to test our analysis code for studying suppressed warnings.
The focus here is on
 * Python repositories
 * Pylint
 * The repositories with 2 side branches
 * Cover 6 different case:
     * File add (meanwhile add suppression) (0->x)
     * File delete (meanwhile delete suppression) (x->0)
     * File rename
     * Single warning type suppression, delete (1->0)
     * Multiple warning types suppression, inline delete (2->1)
     * Multiple warning types suppression, inline add (1->2)
     * Never removed (1->1)

## Ground truth of this repository
 * Totally with 3 branches:
     * main
     * side-a
     * side-b
## Expected output of our analysis scripts

#### File concatenate_strings.py
* **Suppression #1**: # pylint: disable=W1401
  * Introduced in commit e4ddb66e (**file add**), side-a branch
  * Removed in commit 1b99baab, main branch

* **Suppression #2**: # pylint: disable=W1402
  * Introduced in commit ac8f336a, side-a branch
  * Removed in commit b429c023 (**file delete**), main branch

#### File read_files.py
* **Suppression #3**: # pylint: disable=W0702
  * Introduced in commit 7b631b93, main branch
  * Removed in commit 5df1ecbf, side-b branch

* **Suppression #4**: # pylint: disable=unused-variable
  * Introduced in commit 3e859470, main branch
  * Never removed