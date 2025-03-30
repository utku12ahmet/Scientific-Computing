import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def calculate_false_rates(total_population, disease_prevalence, sensitivity, specificity):   
    # Number of actual diseased and healthy individuals
    actual_diseased = total_population * disease_prevalence
    actual_healthy = total_population - actual_diseased
    
    # False negatives: Diseased individuals who test negative
    false_negatives = actual_diseased * (1 - sensitivity)
    
    # False positives: Healthy individuals who test positive
    false_positives = actual_healthy * (1 - specificity)

    plt.figure(figsize=(5,5))
    venn = venn2(subsets=(actual_diseased, actual_healthy, false_positives + false_negatives), 
             set_labels=('Gerçek Negatifler (TN)', 'Gerçek Pozitifler (TP)'))
    
    # Değerleri ekleyelim
    venn.get_label_by_id('10').set_text(f'TN: { actual_healthy}')
    venn.get_label_by_id('01').set_text(f'TP: {actual_diseased}')
    venn.get_label_by_id('11').set_text(f'FP+FN: {false_positives + false_negatives}')

# Başlık ekleyelim
    plt.title("Sınıflandırma Hata Analizi (Venn Diagram)")

# Grafiği göster
    plt.show()
    
    return false_positives, false_negatives
'''
total_population = 100000
disease_prevalence = 0.01  # 1% of the population has the disease
sensitivity = 0.95  # 95% of sick people test positive
specificity = 0.90  # 90% of healthy people test negative
'''

total_population=int(input("total population ?"))
disease_prevalence=float(input("disease_prevalence"))
sensitivity=float(input("sensitivity(false positive)"))
specificity=float(input("specificity(false negative)"))

false_positive_count, false_negative_count = calculate_false_rates(
    total_population, disease_prevalence, sensitivity, specificity
)


print(f"False Positives: {false_positive_count}")
print(f"False Negatives: {false_negative_count}")