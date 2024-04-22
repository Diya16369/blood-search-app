import streamlit as st

# Sample list of donors with their details
donors = [
    {'Name': 'John', 'Area': 'Mumbai', 'Contact': '123-456-7890', 'Blood Group': 'A+'},
    {'Name': 'Alice', 'Area': 'Pune', 'Contact': '456-789-0123', 'Blood Group': 'B+'},
    {'Name': 'Bob', 'Area': 'Thane', 'Contact': '789-012-3456', 'Blood Group': 'O+'},
    {'Name': 'Emily', 'Area': 'Pune', 'Contact': '012-345-6789', 'Blood Group': 'AB+'},
    {'Name': 'David', 'Area': 'Mumbai', 'Contact': '345-678-9012', 'Blood Group': 'A-'},
    {'Name': 'Charlie', 'Area': 'Thane', 'Contact': '678-901-2345', 'Blood Group': 'B-'},
    {'Name': 'Fiona', 'Area': 'Pune', 'Contact': '901-234-5678', 'Blood Group': 'O-'},
    {'Name': 'George', 'Area': 'Mumbai', 'Contact': '234-567-8901', 'Blood Group': 'AB-'},
    {'Name': 'Harry', 'Area': 'Thane', 'Contact': '567-890-1234', 'Blood Group': 'A+'},
    {'Name': 'Irene', 'Area': 'Pune', 'Contact': '890-123-4567', 'Blood Group': 'B+'},
    {'Name': 'Kim', 'Area': 'Mumbai', 'Contact': '123-456-7890', 'Blood Group': 'O+'},
    {'Name': 'Liam', 'Area': 'Mumbai', 'Contact': '345-678-9012', 'Blood Group': 'A+'},
    {'Name': 'Olivia', 'Area': 'Pune', 'Contact': '678-901-2345', 'Blood Group': 'B+'},
    {'Name': 'Noah', 'Area': 'Thane', 'Contact': '901-234-5678', 'Blood Group': 'O+'},
    {'Name': 'Emma', 'Area': 'Mumbai', 'Contact': '234-567-8901', 'Blood Group': 'AB+'},
    {'Name': 'Sophia', 'Area': 'Pune', 'Contact': '567-890-1234', 'Blood Group': 'A-'},
    {'Name': 'Ava', 'Area': 'Thane', 'Contact': '890-123-4567', 'Blood Group': 'B-'},
    {'Name': 'Isabella', 'Area': 'Mumbai', 'Contact': '123-456-7890', 'Blood Group': 'O-'},
    {'Name': 'Mia', 'Area': 'Pune', 'Contact': '456-789-0123', 'Blood Group': 'AB-'},
    {'Name': 'James', 'Area': 'Thane', 'Contact': '789-012-3456', 'Blood Group': 'A+'},
    {'Name': 'Benjamin', 'Area': 'Mumbai', 'Contact': '012-345-6789', 'Blood Group': 'B+'},
    {'Name': 'Lucas', 'Area': 'Pune', 'Contact': '345-678-9012', 'Blood Group': 'O+'},
    {'Name': 'Henry', 'Area': 'Thane', 'Contact': '678-901-2345', 'Blood Group': 'AB+'},
    {'Name': 'Alexander', 'Area': 'Mumbai', 'Contact': '901-234-5678', 'Blood Group': 'A-'},
    {'Name': 'Sebastian', 'Area': 'Pune', 'Contact': '234-567-8901', 'Blood Group': 'B-'},
    {'Name': 'Jack', 'Area': 'Thane', 'Contact': '567-890-1234', 'Blood Group': 'O-'},
    {'Name': 'Daniel', 'Area': 'Mumbai', 'Contact': '890-123-4567', 'Blood Group': 'AB-'},
    {'Name': 'William', 'Area': 'Pune', 'Contact': '123-456-7890', 'Blood Group': 'A+'},
    {'Name': 'Matthew', 'Area': 'Thane', 'Contact': '456-789-0123', 'Blood Group': 'B+'},
    {'Name': 'Joseph', 'Area': 'Mumbai', 'Contact': '789-012-3456', 'Blood Group': 'O+'},
    {'Name': 'Michael', 'Area': 'Pune', 'Contact': '012-345-6789', 'Blood Group': 'AB-'}
]

def search_donors(area, blood_group):
    found_donors = [donor for donor in donors if donor['Area'].lower() == area.lower() and donor['Blood Group'] == blood_group]
    return found_donors

def main():
    st.title('Blood Donor Search')

    # Sidebar for searching donors by area and blood group
    st.sidebar.header('Search Donors')
    search_area = st.sidebar.selectbox('Select Area', sorted(list(set([donor['Area'] for donor in donors]))))
    search_blood_group = st.sidebar.selectbox('Select Blood Group', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    if st.sidebar.button('Search'):
        if search_area:
            search_result = search_donors(search_area, search_blood_group)
            if search_result:
                st.write('Donors found in', search_area, 'with blood group', search_blood_group, ':')
                for donor in search_result:
                    st.write('Name:', donor['Name'], '| Contact:', donor['Contact'], '| Blood Group:', donor['Blood Group'])
            else:
                st.warning('No donors found in {} with blood group {}'.format(search_area, search_blood_group))
        else:
            st.warning('Please select an area to search.')

if __name__ == '__main__':
    main()

