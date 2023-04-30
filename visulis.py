# # # Import necessary libraries
# # import matplotlib.pyplot as plt
# # from flask import Flask, render_template, send_file

# # # Create Flask application
# # app = Flask(__name__)

# # # Route to display the visualization
# # @app.route('/')
# # def show_visualization():
# #     # Generate or load your data
# #     x = [1, 2, 3, 4, 5]
# #     y = [2, 4, 6, 8, 10]
    
# #     # Create the plot
# #     plt.plot(x, y)
# #     plt.xlabel('X-axis')
# #     plt.ylabel('Y-axis')
# #     plt.title('My Plot')
    
# #     # Save the plot as an image file
# #     plot_path = 'static/images/plot.png'
# #     plt.savefig(plot_path)
    
# #     # Clear the plot
# #     plt.clf()
    
# #     # Render the HTML template with the image path
# #     return render_template('index.html', plot_path=plot_path)

# # # Route to serve the image file
# # @app.route('/static/images/plot.png')
# # def serve_image():
# #     return send_file('static/images/plot.png')

# # # Run the Flask application
# # if __name__ == '__main__':
# #     app.run()




# import plotly.express as px
# from flask import Flask, render_template, url_for
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import math
# import seaborn as sns

# app = Flask(__name__)

# @app.route('/visulisation')
# def visulisation():
#     df = pd.read_csv("Data/crop_yield_data.csv")
#     # Create your Plotly Express visualization
#     fig = px.bar(df, x='Year', y='Export Quantity')

#     # Convert the figure to JSON
#     graphJSON = fig.to_json()

#     fig2 = px.bar(df, x='Yield', y='Crop')
#     graphJSON2 = fig2.to_json()


#     # Render the HTML template with the graphJSON
#     return render_template('visulisation.html', graphJSON=graphJSON, graphJSON2=graphJSON2)


# if __name__ == '__main__':
#     app.run(debug=True)
