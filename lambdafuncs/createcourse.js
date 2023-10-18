'use strict';

console.log('Loading function');

export const handler = function(event, context, callback) {
    // Parse the input for the class, days, professor, and major property values
    let className = event.class === undefined ? 'Unknown Class' : event.class;
    let classDays = event.days === undefined ? 'Unknown Days' : event.days;
    let professor = event.professor === undefined ? 'Unknown Professor' : event.professor;
    let major = event.major === undefined ? 'Unknown Major' : event.major;

    // Construct the "Class Added" message
    let classAddedMessage = `Class Added: ${className}, taught by Professor ${professor}.`;
    classAddedMessage += ` This class is scheduled for ${classDays} and the major is ${major}.`;

    // Log the message to CloudWatch
    console.log(classAddedMessage);
    
    // Return the "Class Added" message to the caller as a JSON object
    callback(null, {
        "message": classAddedMessage
    });
};