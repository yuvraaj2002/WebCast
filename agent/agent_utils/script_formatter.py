def format_podcast_script(script_data):
    """
    Format podcast script data into a readable format with speaker labels.
    
    Args:
        script_data (dict): Dictionary containing episode metadata and podcast script
        
    Returns:
        str: Formatted script with speaker labels and metadata
    """
    # Extract metadata and script
    metadata = script_data.get('episode_metadata', {})
    script = script_data.get('podcast_script', [])
    
    # Format metadata section
    formatted_script = f"""Episode: {metadata.get('title', 'Untitled')}
Original Title: {metadata.get('original_title', 'N/A')}
Author: {metadata.get('author', 'N/A')}
Duration: {metadata.get('duration_minutes', 'N/A')} minutes
Domain: {metadata.get('content_domain', 'N/A')}

Summary:
{metadata.get('summary', 'No summary available')}

Script:
"""
    
    # Format script section
    for entry in script:
        speaker = entry['speaker']
        text = entry['text']
        formatted_script += f"\n{speaker}: {text}\n"
    
    return formatted_script


if __name__ == "__main__":
    # Example usage with the new format
    script_data = {
        "episode_metadata": {
            "title": "Translation Matters: Nietzsche's \"Nothingness\" vs. \"Oblivion\"",
            "original_title": "\"Nothingness\" and \"Oblivion\" in \"The Genealogy of Morals,\" Essay III, Section 28",
            "author": "Dr. Alexander Riegel",
            "duration_minutes": 15,
            "summary": "This episode examines a specific passage from Nietzsche's 'On the Genealogy of Morals'...",
            "content_domain": "Philosophy"
        },
        "podcast_script": [
            {
                "speaker": "Host",
                "text": "Welcome to BlogCast! Today we're diving into..."
            },
            {
                "speaker": "Co-Host",
                "text": "What caught your attention about this?"
            }
        ]
    }
    formatted_script = format_podcast_script(script_data)
    print(formatted_script)
