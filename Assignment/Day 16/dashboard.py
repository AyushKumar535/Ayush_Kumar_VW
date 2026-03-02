from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    # Get the role from the query parameter, default to 'employee' if not provided
    role = request.args.get('role', 'employee')
    
    # Define content based on the role
    page_title = ''
    nav_links = []
    user_info = ''
    action_buttons = []
    user_name = ''
    
    # Role-based information
    if role == 'admin':
        page_title = 'Admin Dashboard'
        user_name = 'Alice Smith'  # Admin-specific name
        nav_links = [
            {'name': 'Admin Home', 'url': '/dashboard?role=admin'},
            {'name': 'Settings', 'url': '/settings'},
            {'name': 'User Management', 'url': '/users'}
        ]
        user_info = '''
            <p><strong>Name:</strong> Alice Smith</p>
            <p><strong>Position:</strong> Chief Technology Officer</p>
            <p><strong>Salary:</strong> $150,000</p>
        '''
        action_buttons = ['Update Info', 'Delete User']
        
    elif role == 'manager':
        page_title = 'Manager Dashboard'
        user_name = 'Bob Johnson'  # Manager-specific name
        nav_links = [
            {'name': 'Manager Home', 'url': '/dashboard?role=manager'},
            {'name': 'Team', 'url': '/team'}
        ]
        user_info = '''
            <p><strong>Name:</strong> Bob Johnson</p>
            <p><strong>Position:</strong> Engineering Manager</p>
            <p><strong>Salary:</strong> $110,000</p>
        '''
        action_buttons = ['Update Info', 'View Team']
        
    elif role == 'employee':
        page_title = 'Employee Dashboard'
        user_name = 'Charlie Davis'  # Employee-specific name
        nav_links = [
            {'name': 'Employee Home', 'url': '/dashboard?role=employee'},
            {'name': 'Profile', 'url': '/profile'}
        ]
        user_info = '''
            <p><strong>Name:</strong> Charlie Davis</p>
            <p><strong>Position:</strong> Software Engineer</p>
        '''
        action_buttons = ['Update Info']
        
    # Render the template with the dynamic content
    return render_template(
        'dashboard.html',  # The HTML template to use
        page_title=page_title,
        nav_links=nav_links,
        user_info=user_info,
        action_buttons=action_buttons,
        user_name=user_name
    )

if __name__ == '__main__':
    app.run(debug=True)