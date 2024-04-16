document.addEventListener('DOMContentLoaded', function () {
    // Fetch property types and populate the dropdown
    fetch('/get_unique_property_types')
        .then(response => response.json())
        .then(data => {
            const propertyTypeDropdown = document.getElementById('property-type-dropdown');

            // Add options to the dropdown
            data.unique_property_types.forEach(propertyType => {
                const option = document.createElement('option');
                option.value = propertyType;
                option.text = propertyType;
                propertyTypeDropdown.add(option);
            });
        })
        .catch(error => console.error('Error fetching property types:', error));

    // Add an event listener for the "View Details" button
    document.getElementById('view-details-btn').addEventListener('click', function () {
        const selectedPropertyType = document.getElementById('property-type-dropdown').value;

        // Send a POST request to get the listing details
        fetch('/get_listing_details', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `selected_property_type=${selectedPropertyType}`,
        })
            .then(response => response.json())
            .then(data => {
                // Update the details on the page
                document.getElementById('listing-url').innerText = `Listing URL: ${data.listing_url}`;
                document.getElementById('description').innerText = `Description: ${data.description}`;
                document.getElementById('pictures').innerText = `Pictures: ${data.picture_url}`;
                document.getElementById('host-name').innerText = `Host Name: ${data.host_name}`;
                document.getElementById('amenities').innerText = `Amenities: ${data.amenities}`;
            })
            .catch(error => console.error('Error:', error));
    });
});
