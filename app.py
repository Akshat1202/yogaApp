import os
from flask import Flask, request, jsonify

from landmark_coordinates import get_landmark_coordinates
from suryanamaskar import evaluate_surya_namaskar_pose

UPLOAD_FOLDER = 'upload_images'

    
app = Flask(__name__, template_folder="template")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/get_array', methods=['POST'])
def get_array():
    if request.method == 'POST':
        if 'file' in request.files:
            image = request.files['file']
            if image is not None:    
                flanme = image.filename
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], flanme)
                image.save(image_path)
                data_to_send = get_landmark_coordinates(image_path)
                if data_to_send is not None:
                    
                    # find suggestions for yoga asana
                    suggestions = evaluate_surya_namaskar_pose(data_to_send)
                    
                    return jsonify(suggestions)
                else:
                    print("Error: Failed to process the image")
                    return "Error: Failed to process the image", 500
            else:
                print("Error: No valid image provided in the request")
                return "Error: No valid image provided in the request", 400
        else:
            print("Error: 'image' not found in the request")
            return "Error: 'image' not found in the request", 400
    else:
        print("Error: Invalid request method")
        return "Error: Invalid request method", 405
      

@app.errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


