import os
from flask import Flask, render_template, request, jsonify

from landmark_coordinates import get_landmark_coordinates
from suryanamaskar import evaluate_surya_namaskar_pose
from vakrasan import evaluate_vakrasana_pose

UPLOAD_FOLDER = 'upload_images'

    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_array', methods=['POST'])
def get_array():
    if request.method == 'POST':
        if 'file' in request.files:
            image = request.files['file']
            if image is not None:    
                flanme = image.filename
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], flanme)
                image.save(image_path)
                try:
                    data_to_send = get_landmark_coordinates(image_path)
                    suggestions = evaluate_surya_namaskar_pose(data_to_send)   
                    return render_template('result.html', suggestions=suggestions)
                
                except Exception as e:
                        print(f"Error processing image: {e}")
                        return jsonify({
                            'success': False,
                            'message': 'Failed to process the image'
                        }), 500
            else:
                print("Error: No valid image provided in the request")
                return jsonify({
                    'success': False,
                    'message': 'No valid image provided in the request'
                }), 400
        else:
            print("Error: 'image' not found in the request")
            return jsonify({
                'success': False,
                'message': 'image not found in the request'
            }), 400
    else:
        print("Error: Invalid request method")
        return jsonify({
            'success': False,
            'message': 'Invalid request method'
        }), 405
      

@app.errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


