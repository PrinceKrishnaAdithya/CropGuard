import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# MODEL 1 DATA
# -----------------------------
data1 = [
("Apple___Apple_scab",1.00,0.95,0.97,91),
("Apple___Black_rot",0.98,1.00,0.99,87),
("Apple___Cedar_apple_rust",0.95,1.00,0.97,37),
("Apple___healthy",0.99,1.00,0.99,270),
("Blueberry___healthy",0.98,1.00,0.99,198),
("Cherry_(including_sour)___Powdery_mildew",1.00,0.98,0.99,176),
("Cherry_(including_sour)___healthy",0.99,1.00,1.00,125),
("Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",0.85,0.93,0.89,71),
("Corn_(maize)___Common_rust_",0.99,0.99,0.99,168),
("Corn_(maize)___Northern_Leaf_Blight",0.97,0.91,0.94,147),
("Corn_(maize)___healthy",0.98,1.00,0.99,168),
("Grape___Black_rot",1.00,0.97,0.99,171),
("Grape___Esca_(Black_Measles)",0.99,1.00,1.00,220),
("Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",0.99,0.99,0.99,159),
("Grape___healthy",0.98,1.00,0.99,52),
("Orange___Haunglongbing_(Citrus_greening)",1.00,1.00,1.00,805),
("Peach___Bacterial_spot",0.99,0.99,0.99,387),
("Peach___healthy",0.98,0.96,0.97,54),
("Pepper,_bell___Bacterial_spot",1.00,0.86,0.92,157),
("Pepper,_bell___healthy",0.95,1.00,0.97,237),
("Potato___Early_blight",1.00,0.97,0.99,156),
("Potato___Late_blight",0.98,0.96,0.97,144),
("Potato___healthy",0.95,0.91,0.93,22),
("Raspberry___healthy",1.00,1.00,1.00,59),
("Soybean___healthy",1.00,1.00,1.00,757),
("Squash___Powdery_mildew",1.00,1.00,1.00,267),
("Strawberry___Leaf_scorch",0.99,0.98,0.98,163),
("Strawberry___healthy",1.00,1.00,1.00,71),
("Tomato___Bacterial_spot",0.99,0.85,0.91,317),
("Tomato___Early_blight",0.76,0.88,0.82,170),
("Tomato___Late_blight",0.94,0.97,0.96,288),
("Tomato___Leaf_Mold",0.99,0.95,0.97,159),
("Tomato___Septoria_leaf_spot",0.88,0.99,0.93,273),
("Tomato___Spider_mites Two-spotted_spider_mite",0.96,0.99,0.97,237),
("Tomato___Target_Spot",0.95,0.92,0.93,191),
("Tomato___Tomato_Yellow_Leaf_Curl_Virus",1.00,0.99,0.99,796),
("Tomato___Tomato_mosaic_virus",0.88,0.98,0.93,46),
("Tomato___healthy",1.00,0.98,0.99,251),
]

# -----------------------------
# MODEL 2 DATA
# -----------------------------
data2 = [
("Apple___Apple_scab",1.00,0.96,0.98,98),
("Apple___Black_rot",1.00,1.00,1.00,103),
("Apple___Cedar_apple_rust",0.98,0.99,0.99,179),
("Apple___healthy",0.98,0.97,0.97,219),
("Blueberry___healthy",0.99,0.94,0.96,217),
("Cherry_(including_sour)___Powdery_mildew",0.99,1.00,0.99,165),
("Cherry_(including_sour)___healthy",0.98,0.95,0.97,133),
("Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",0.84,0.86,0.85,78),
("Corn_(maize)___Common_rust_",0.99,1.00,1.00,183),
("Corn_(maize)___Northern_Leaf_Blight",0.93,0.93,0.93,152),
("Corn_(maize)___healthy",1.00,0.99,1.00,162),
("Grape___Black_rot",0.96,1.00,0.98,162),
("Grape___Esca_(Black_Measles)",1.00,0.98,0.99,202),
("Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",1.00,0.99,1.00,181),
("Grape___healthy",0.99,0.99,0.99,192),
("Orange___Haunglongbing_(Citrus_greening)",0.97,1.00,0.99,810),
("Peach___Bacterial_spot",0.99,0.99,0.99,335),
("Peach___healthy",0.99,0.99,0.99,195),
("Pepper,_bell___Bacterial_spot",0.93,1.00,0.97,154),
("Pepper,_bell___healthy",1.00,0.98,0.99,248),
("Potato___Early_blight",0.99,0.97,0.98,151),
("Potato___Late_blight",0.99,0.90,0.94,156),
("Potato___healthy",0.98,0.98,0.98,180),
("Raspberry___healthy",0.97,0.92,0.95,39),
("Soybean___healthy",0.99,1.00,0.99,782),
("Squash___Powdery_mildew",1.00,0.99,0.99,258),
("Strawberry___Leaf_scorch",1.00,0.98,0.99,181),
("Strawberry___healthy",1.00,0.98,0.99,170),
("Tomato___Bacterial_spot",0.95,0.97,0.96,324),
("Tomato___Early_blight",0.88,0.94,0.91,136),
("Tomato___Late_blight",0.92,0.96,0.94,272),
("Tomato___Leaf_Mold",0.97,0.96,0.96,117),
("Tomato___Septoria_leaf_spot",0.99,0.90,0.95,268),
("Tomato___Spider_mites Two-spotted_spider_mite",0.88,0.97,0.93,233),
("Tomato___Target_Spot",0.98,0.83,0.90,232),
("Tomato___Tomato_Yellow_Leaf_Curl_Virus",0.97,1.00,0.98,836),
("Tomato___Tomato_mosaic_virus",0.98,0.97,0.97,182),
("Tomato___healthy",1.00,0.97,0.98,236),
]

# -----------------------------
# CREATE DATAFRAMES
# -----------------------------
columns = ["Class","Precision","Recall","F1","Support"]
df1 = pd.DataFrame(data1, columns=columns)
df2 = pd.DataFrame(data2, columns=columns)

# Merge for comparison
df = df1.merge(df2, on="Class", suffixes=("_Model1","_Model2"))

# -----------------------------
# PLOT 1: F1 SCORE COMPARISON
# -----------------------------
plt.figure()
plt.plot(df["F1_Model1"], label="Model 1")
plt.plot(df["F1_Model2"], label="Model 2")
plt.title("F1 Score Comparison")
plt.legend()
plt.xticks([])
plt.show()

# -----------------------------
# PLOT 2: PRECISION
# -----------------------------
plt.figure()
plt.plot(df["Precision_Model1"], label="Model 1")
plt.plot(df["Precision_Model2"], label="Model 2")
plt.title("Precision Comparison")
plt.legend()
plt.xticks([])
plt.show()

# -----------------------------
# PLOT 3: RECALL
# -----------------------------
plt.figure()
plt.plot(df["Recall_Model1"], label="Model 1")
plt.plot(df["Recall_Model2"], label="Model 2")
plt.title("Recall Comparison")
plt.legend()
plt.xticks([])
plt.show()

# -----------------------------
# PLOT 4: SUPPORT DISTRIBUTION
# -----------------------------
plt.figure()
plt.bar(range(len(df)), df["Support_Model1"], label="Model 1")
plt.bar(range(len(df)), df["Support_Model2"], label="Model 2")
plt.title("Support Comparison")
plt.legend()
plt.xticks([])
plt.show()

# -----------------------------
# PLOT 5: OVERALL AVERAGE
# -----------------------------
avg = pd.DataFrame({
    "Metric": ["Precision","Recall","F1"],
    "Model1":[df["Precision_Model1"].mean(), df["Recall_Model1"].mean(), df["F1_Model1"].mean()],
    "Model2":[df["Precision_Model2"].mean(), df["Recall_Model2"].mean(), df["F1_Model2"].mean()]
})

avg.set_index("Metric").plot(kind="bar")
plt.title("Overall Model Performance")
plt.show()