import matplotlib.pyplot as plt
import numpy as np

def parke_error_grid(ref_values, pred_values, title_string):
  # Create a larger figure with Seaborn styling
  # plt.figure(figsize=(10, 8))
  # Clear plot
  plt.clf()

  # Set up plot
  plt.scatter(ref_values, pred_values, marker='o', color='black', s=8)
  plt.title(title_string + " Parkes Error Grid")#,fontsize=28)
  plt.xlabel("Reference Concentration (mg/dl)")#,fontsize=24)
  plt.ylabel("Prediction Concentration (mg/dl)")#,fontsize=24)
  plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400,450,500,550])#,fontsize=16)
  plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400,450,500,550])#,fontsize=16)

  plt.gca().set_facecolor('white')

  # Set axes lengths
  plt.gca().set_xlim([0, 550])
  plt.gca().set_ylim([0, 550])
  plt.gca().set_aspect((550)/(550))

  # Plot zone lines
  plt.plot([0, 550], [0, 550], ':', c='black')
  # Category B 
  #lower
  plt.plot([50, 50], [0, 30], '--', c='black')
  plt.plot([50, 90], [30, 80], '--', c='black')
  plt.plot([90, 330], [80, 230], '--', c='black')
  plt.plot([330, 550], [230, 450], '--', c='black')
  #upper
  plt.plot([0, 30], [50, 50], '--', c='black')
  plt.plot([30, 230], [50, 330], '--', c='black')
  plt.plot([230, 440], [330, 550], '--', c='black')

  # Category C
  #lower
  plt.plot([90, 260], [0, 130], '--', c='black')
  plt.plot([260, 550], [130, 250], '--', c='black')
  #upper
  plt.plot([0, 30], [60, 60], '--', c='black')
  plt.plot([30, 280], [60, 550], '--', c='black')

  # # Category D
  #lower
  plt.plot([250, 250], [0, 40], '--', c='black')
  plt.plot([250, 410], [40, 110], '--', c='black')
  plt.plot([410, 550], [110, 160], '--', c='black')
  #upper
  plt.plot([0, 25], [80, 80], '--', c='black')
  plt.plot([25, 35], [80, 90], '--', c='black')
  plt.plot([35, 125], [90, 550], '--', c='black')

  # Category E
  # upper only 
  plt.plot([0, 35], [200, 200], '--', c='black')
  plt.plot([35, 50], [200, 550], '--', c='black')

  # Add zone titles with specified colors
  plt.text(500, 450, "A")#, fontsize=18)
  plt.text(450, 500, "A")#, fontsize=18)
  plt.text(500, 300, "B")#, fontsize=18)
  plt.text(300, 500, "B")#, fontsize=18)
  plt.text(500, 180, "C")#, fontsize=18)
  plt.text(160, 500, "C")#, fontsize=18)
  plt.text(500, 50, "D")#, fontsize=18)
  plt.text(70, 500, "D")#, fontsize=18)
  plt.text(10, 500, "E")#, fontsize=18)
  plt.show()
if __name__ == "__main__":
    # Test data
    ref_values = np.array([50, 100, 150, 200, 250, 300, 350, 400])
    pred_values = np.array([60, 110, 140, 190, 260, 290, 340, 410])

    # Generate and display the plot
    parke_error_grid(ref_values, pred_values, "Test")
    plt.show()
