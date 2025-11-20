from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Road safety knowledge base
INTERVENTIONS = {
    'curve': '''**Sharp Curve Safety Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Install Curve Warning Signs (IRC:67)
   - Place advance curve warning signs 100-150m before curve
   - Use reflective materials for night visibility

2. Install Chevron Alignment Markers (IRC:35)
   - Place reflective chevrons on outer edge of curve
   - Spacing: 40m on highways, 20m on dangerous curves

3. Improve Road Lighting (IRC:SP:84)
   - Install high-mast LED lights with minimum 20 lux
   - Focus on curve entry and exit points

4. Apply Anti-skid Surface Treatment
   - Use textured pavement for better tire grip
   - Regular maintenance to prevent wear

5. Install Speed Reduction Measures (IRC:99)
   - Speed breakers before curve entry
   - Rumble strips as warning

**ESTIMATED COST:** ₹8-15 lakhs for 1km stretch
**IMPLEMENTATION TIMELINE:** 2-3 months
**IRC REFERENCES:** IRC:35, IRC:67, IRC:99, IRC:SP:84''',
    
    'school': '''**School Zone Safety Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Install School Zone Signs (IRC:67)
   - Fluorescent yellow-green warning signs
   - "SCHOOL ZONE - SLOW" markings

2. Create Pedestrian Crossings (IRC:35)
   - Zebra crossings with warning lights
   - Push-button activated signals

3. Install Speed Control Measures (IRC:99)
   - Multiple speed humps in 500m zone
   - Speed limit: 25-30 km/h

4. Deploy Traffic Management
   - Traffic marshals during school hours
   - Designated drop-off zones

5. Implement Safety Infrastructure
   - Pedestrian barriers/fencing
   - CCTV surveillance

**ESTIMATED COST:** ₹5-10 lakhs per school zone
**IMPLEMENTATION TIMELINE:** 1-2 months
**IRC REFERENCES:** IRC:35, IRC:67, IRC:99''',
    
    'speed': '''**Speed Control Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Install Speed Limit Signs (IRC:67)
   - Clear speed limit signage every 500m
   - Reflective for night visibility

2. Deploy Automated Enforcement
   - Speed cameras at strategic locations
   - Red light violation detection

3. Install Physical Speed Calming (IRC:99)
   - Rumble strips before high-risk zones
   - Speed breakers at appropriate intervals

4. Road Design Modifications
   - Optical narrowing using road markings
   - Chicanes in residential areas

5. Enhanced Visibility Measures
   - LED speed display boards
   - Warning flashers

**ESTIMATED COST:** ₹10-20 lakhs for 2km stretch
**IMPLEMENTATION TIMELINE:** 1-3 months
**IRC REFERENCES:** IRC:67, IRC:99, IRC:SP:87''',
    
    'intersection': '''**Intersection Safety Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Install Modern Traffic Signals (IRC:93)
   - LED signals with countdown timers
   - All-red phase for safety

2. Improve Visibility (IRC:SP:84)
   - High-intensity street lights at intersection
   - Clear sight distance maintenance

3. Enhanced Road Markings (IRC:35)
   - Reflective thermoplastic markings
   - Stop lines and directional arrows

4. Surveillance and Enforcement
   - CCTV cameras for monitoring
   - Red light violation detection

5. Pedestrian Safety Infrastructure
   - Safe waiting islands
   - Dedicated pedestrian signals

**ESTIMATED COST:** ₹15-30 lakhs per intersection
**IMPLEMENTATION TIMELINE:** 2-4 months
**IRC REFERENCES:** IRC:35, IRC:93, IRC:SP:84''',
    
    'night': '''**Night-time Safety Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Install Street Lighting (IRC:SP:84)
   - High-mast LED lights with minimum 15 lux
   - Energy-efficient solar options

2. Apply Reflective Road Markings (IRC:35)
   - Cat-eye reflectors at 10m intervals
   - High-reflectivity thermoplastic paint

3. Install Delineators
   - Reflective poles along road edges
   - Curve delineation markers

4. Improve Sign Reflectivity (IRC:67)
   - Use high-intensity reflective sheets (Type III/IV)
   - Regular cleaning and maintenance

5. Vegetation Management
   - Clear obstructions blocking light
   - Maintain 50m visibility at curves

**ESTIMATED COST:** ₹8-18 lakhs per km
**IMPLEMENTATION TIMELINE:** 1-2 months
**IRC REFERENCES:** IRC:35, IRC:67, IRC:SP:84'''
}

def analyze_query(query):
    query_lower = query.lower()
    
    if any(word in query_lower for word in ['curve', 'bend', 'turn', 'winding']):
        return INTERVENTIONS['curve']
    elif any(word in query_lower for word in ['school', 'children', 'student']):
        return INTERVENTIONS['school']
    elif any(word in query_lower for word in ['speed', 'fast', 'racing']):
        return INTERVENTIONS['speed']
    elif any(word in query_lower for word in ['intersection', 'junction', 'signal']):
        return INTERVENTIONS['intersection']
    elif any(word in query_lower for word in ['night', 'dark', 'visibility', 'fog']):
        return INTERVENTIONS['night']
    else:
        return '''**General Road Safety Interventions (IRC Standards)**

RECOMMENDED INTERVENTIONS:

1. Conduct Road Safety Audit (IRC:SP:88)
2. Improve Road Markings (IRC:35)
3. Install Warning Signs (IRC:67)
4. Enhance Lighting (IRC:SP:84)
5. Regular Maintenance Program

**ESTIMATED COST:** ₹10-20 lakhs
**TIMELINE:** 2-4 months'''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'success': False, 'error': 'No query provided'})
        
        response_text = analyze_query(query)
        
        return jsonify({'success': True, 'response': response_text})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("   ROAD SAFETY GPT - OFFLINE MODE")
    print("   No API Key Required!")
    print("   Server starting at http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)