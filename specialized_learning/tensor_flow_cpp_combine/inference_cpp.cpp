#include <iostream>
#include <memory>
#include <vector>
#include "tensorflow/lite/interpreter.h"
#include "tensorflow/lite/kernels/register.h"
#include "tensorflow/lite/model.h"

int main() {
    const char* model_path = "lstm_model.tflite";

    // Load model
    auto model = tflite::FlatBufferModel::BuildFromFile(model_path);
    if (!model) {
        std::cerr << "Failed to load model: " << model_path << std::endl;
        return -1;
    }

    // Build interpreter
    tflite::ops::builtin::BuiltinOpResolver resolver;
    std::unique_ptr<tflite::Interpreter> interpreter;
    tflite::InterpreterBuilder(*model, resolver)(&interpreter);
    if (!interpreter) {
        std::cerr << "Failed to create interpreter" << std::endl;
        return -1;
    }

    // Allocate tensors
    if (interpreter->AllocateTensors() != kTfLiteOk) {
        std::cerr << "Failed to allocate tensors" << std::endl;
        return -1;
    }

    // Get input tensor info
    float* input = interpreter->typed_input_tensor<float>(0);

    // Prepare input: [47, 48, 49] reshaped as (1,3,1)
    input[0] = 47.0f;
    input[1] = 48.0f;
    input[2] = 49.0f;

    // Run inference
    if (interpreter->Invoke() != kTfLiteOk) {
        std::cerr << "Failed to run inference" << std::endl;
        return -1;
    }

    // Read output
    float* output = interpreter->typed_output_tensor<float>(0);
    std::cout << "Predicted next value after [47,48,49]: " << output[0] << std::endl;

    return 0;
}
