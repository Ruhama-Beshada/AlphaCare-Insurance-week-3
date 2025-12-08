import numpy as np
from scipy import stats
import statsmodels.stats.proportion as smp

def proportion_test(group1_vals, group2_vals):
    """Z-test for difference in proportions"""
    count = np.array([group1_vals.sum(), group2_vals.sum()])
    nobs = np.array([len(group1_vals), len(group2_vals)])
    stat, pval = smp.proportions_ztest(count, nobs)
    return stat, pval

def two_sample_t_or_mannwhitney(a, b, alpha=0.05):
    """Choose t-test or Mann-Whitney based on normality"""
    normal = False
    if len(a) < 500 or len(b) < 500:
        try:
            pa = stats.shapiro(a).pvalue
            pb = stats.shapiro(b).pvalue
            normal = (pa > alpha) and (pb > alpha)
        except:
            normal = False
    if normal:
        levene_p = stats.levene(a, b).pvalue
        equal_var = True if levene_p > alpha else False
        stat, pval = stats.ttest_ind(a, b, equal_var=equal_var, nan_policy='omit')
        test_name = "t-test"
    else:
        stat, pval = stats.mannwhitneyu(a, b, alternative='two-sided')
        test_name = "Mann-Whitney U"
    return test_name, stat, pval

def anova_or_kruskal(groups):
    """ANOVA if possible, else Kruskal-Wallis"""
    try:
        stat, p = stats.f_oneway(*groups)
        test_name = "ANOVA"
    except:
        stat, p = stats.kruskal(*groups)
        test_name = "Kruskal-Wallis"
    return test_name, stat, p
