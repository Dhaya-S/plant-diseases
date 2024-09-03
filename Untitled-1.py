def pred_tomato_dieas(tomato_plant):
    test_image = load_img(tomato_plant, target_size=(128, 128))
    test_image = img_to_array(test_image) / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    pred = np.argmax(result, axis=1)
    
    # Define fertilizer recommendations
    fertilizer_recommendations = {
        0: "Use a balanced fertilizer with micronutrients such as 10-10-10 or 20-20-20.",
        1: "Use a high phosphorus fertilizer like 10-20-10.",
        2: "No additional fertilizer needed. Continue regular care.",
        3: "Use a balanced fertilizer with high potassium such as 5-10-10.",
        4: "Use a balanced fertilizer with micronutrients like 10-10-10.",
        5: "Use a balanced fertilizer with high potassium such as 5-10-10.",
        6: "Use a balanced fertilizer with micronutrients like 10-10-10.",
        7: "Use a balanced fertilizer with high phosphorus like 10-20-10.",
        8: "Use a balanced fertilizer with high potassium such as 5-10-10.",
        9: "Use a balanced fertilizer with micronutrients like 10-10-10."
    }
    
    # Predict and return corresponding page and fertilizer recommendation
    if pred == 0:
        return "Tomato - Bacteria Spot Disease", 'Tomato-Bacteria Spot.html', fertilizer_recommendations[0]
    elif pred == 1:
        return "Tomato - Early Blight Disease", 'Tomato-Early_Blight.html', fertilizer_recommendations[1]
    elif pred == 2:
        return "Tomato - Healthy and Fresh", 'Tomato-Healthy.html', fertilizer_recommendations[2]
    elif pred == 3:
        return "Tomato - Late Blight Disease", 'Tomato-Late_blight.html', fertilizer_recommendations[3]
    elif pred == 4:
        return "Tomato - Leaf Mold Disease", 'Tomato-Leaf_Mold.html', fertilizer_recommendations[4]
    elif pred == 5:
        return "Tomato - Septoria Leaf Spot Disease", 'Tomato-Septoria_leaf_spot.html', fertilizer_recommendations[5]
    elif pred == 6:
        return "Tomato - Target Spot Disease", 'Tomato-Target_Spot.html', fertilizer_recommendations[6]
    elif pred == 7:
        return "Tomato - Tomato Yellow Leaf Curl Virus Disease", 'Tomato-Tomato_Yellow_Leaf_Curl_Virus.html', fertilizer_recommendations[7]
    elif pred == 8:
        return "Tomato - Tomato Mosaic Virus Disease", 'Tomato-Tomato_mosaic_virus.html', fertilizer_recommendations[8]
    elif pred == 9:
        return "Tomato - Two Spotted Spider Mite Disease", 'Tomato-Two_spotted_spider_mite.html', fertilizer_recommendations[9]
