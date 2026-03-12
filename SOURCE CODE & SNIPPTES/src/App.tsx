import React, { useState } from 'react';
import axios from 'axios';
import {
  View,
  TextInput,
  Button,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import Modal from 'react-native-modal';




const symptomsList = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis'
];


interface PredictionData {
  disease: string;
  description: string;
  precautions: string;
}






const App = () => {
  const [symptom, setSymptom] = useState('');
  const [selectedSymptoms, setSelectedSymptoms] = useState<string[]>([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [isModalVisible, setModalVisible] = useState(false);
  const [predictionData, setPredictionData] = useState<PredictionData | null>(null);
 


  const handleInputFocus = () => {
    setShowSuggestions(true);
  };


  const handleSymptomSelect = (selected: string) => {
    if (!selectedSymptoms.includes(selected)) {
      setSelectedSymptoms((prev) => [...prev, selected]);
    }
    setSymptom('');
    setShowSuggestions(false);
  };


  const removeSymptom = (symptomToRemove: string) => {
    setSelectedSymptoms((prev) => prev.filter((symptom) => symptom !== symptomToRemove));
  };


  const handleSubmit = async () => {
    try {
      const symptomsData = selectedSymptoms.slice(0, 17).map((symptom) => {
        const index = symptomsList.indexOf(symptom);
        return index !== -1 ? symptomsList[index] : 'prognosis';
      });


      while (symptomsData.length < 17) {
        symptomsData.push('0');
      }


      const requestData = {
        symptoms: symptomsData,
      };


      console.log('Request Data:', requestData);


      const response = await axios.post('http://192.168.89.118:5000/predict', requestData);
     
      console.log('Prediction Response:', response.data);


      setPredictionData(response.data);
      setModalVisible(true);


    } catch (error) {
      console.error('Error submitting symptoms:', error);
      alert('An error occurred. Please try again.');
    }
  };


  return (
    <View style={styles.container}>
      <View style={styles.topLeftContainer}>
        <View style={styles.greetingBox}>
          <Text style={styles.greetingText}>🩺Welcome to VigorTrack!</Text>
        </View>
      </View>


      <Text style={styles.title}>🦠Disease predictor🦠</Text>


      <View style={styles.selectedSymptomsContainer}>
        {selectedSymptoms.map((symptom, index) => (
          <View key={index} style={styles.symptomBubble}>
            <Text style={styles.symptomText}>{symptom}</Text>
            <TouchableOpacity
              style={styles.deleteButton}
              onPress={() => removeSymptom(symptom)}
            >
              <Text style={styles.deleteText}>⛔</Text>
            </TouchableOpacity>
          </View>
        ))}
      </View>


      <TextInput
        style={styles.input}
        placeholder="📝 Enter at least three symptoms"
        value={symptom}
        onChangeText={setSymptom}
        onFocus={handleInputFocus}
      />


      {showSuggestions && (
        <ScrollView style={styles.suggestionsContainer}>
          {symptomsList.map((suggestion, index) => (
            <TouchableOpacity
              key={index}
              style={styles.suggestionItem}
              onPress={() => handleSymptomSelect(suggestion)}
            >
              <Text>{suggestion}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      )}


      <Button title="🔎 Check Disease" onPress={handleSubmit} />
      <Text style={styles.note}>
        This is only a prediction of the disease based on entered symptoms. For confirmation, contact a doctor.
      </Text>


      {/* Custom Modal */}
      <Modal isVisible={isModalVisible} onBackdropPress={() => setModalVisible(false)}>
  <View style={styles.modalContent}>
    {predictionData && (
      <>
        <Text style={styles.modalTitle}>Predicted Disease: {predictionData.disease}</Text>
        <Text style={styles.modalDescription}>Description: {predictionData.description}</Text>
        <Text style={styles.modalPrecautions}>Precautions: {predictionData.precautions}</Text>
      </>
    )}
    <TouchableOpacity style={styles.closeButton} onPress={() => setModalVisible(false)}>
      <Text style={styles.closeButtonText}>Close</Text>
    </TouchableOpacity>
  </View>
</Modal>


    </View>
  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#aae0f0',
    paddingHorizontal: 20,
  },
  topLeftContainer: {
    position: 'absolute',
    top: 20,
    left: 20,
    flexDirection: 'row',
    alignItems: 'center',
  },
  greetingBox: {
    paddingTop: 40,
  },
  greetingText: {
    fontSize: 28,
    fontWeight: 'bold',
    color: 'black',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20,
  },
  input: {
    height: 50,
    borderColor: '#ccc',
    borderWidth: 1,
    paddingHorizontal: 15,
    marginBottom: 15,
    width: '100%',
    borderRadius: 25,
    backgroundColor: '#fff',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    elevation: 3,
  },
  suggestionsContainer: {
    maxHeight: 200,
    marginBottom: 20,
    backgroundColor: '#fff',
    borderRadius: 10,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  selectedSymptomsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 10,
  },
  symptomBubble: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#000',
    borderRadius: 25,
    paddingVertical: 10,
    paddingHorizontal: 15,
    marginRight: 10,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  symptomText: {
    marginRight: 10,
    fontSize: 16,
    color: '#fff',
  },
  deleteButton: {
    backgroundColor: '#000',
   
  },
  deleteText: {
    color: '#fff',
    fontWeight: 'bold',
  },
  suggestionItem: {
    padding: 15,
    borderBottomWidth: 1,
    borderColor: '#e0e0e0',
    backgroundColor: '#f9f9f9',
  },
  note: {
    textAlign: 'center',
    fontSize: 12,
    marginTop: 5,
    color: '#666',
  },
 
  modalContent: {
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 10,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 2 },
    elevation: 5,
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
    color: '#333',
  },
  modalDescription: {
    fontSize: 16,
    marginBottom: 10,
    color: '#555',
  },
  modalPrecautions: {
    fontSize: 16,
    marginBottom: 20,
    color: '#555',
  },
  closeButton: {
    backgroundColor: '#ff4d4d',
    padding: 10,
    borderRadius: 5,
  },
  closeButtonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
});

export default App;