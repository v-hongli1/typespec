// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package specialwords.models;

import com.azure.core.annotation.Generated;
import com.azure.core.annotation.Immutable;
import com.azure.json.JsonReader;
import com.azure.json.JsonSerializable;
import com.azure.json.JsonToken;
import com.azure.json.JsonWriter;
import java.io.IOException;

/**
 * The SameAsModel model.
 */
@Immutable
public final class SameAsModel implements JsonSerializable<SameAsModel> {
    /*
     * The SameAsModel property.
     */
    @Generated
    private final String sameAsModel;

    /**
     * Creates an instance of SameAsModel class.
     * 
     * @param sameAsModel the sameAsModel value to set.
     */
    @Generated
    public SameAsModel(String sameAsModel) {
        this.sameAsModel = sameAsModel;
    }

    /**
     * Get the sameAsModel property: The SameAsModel property.
     * 
     * @return the sameAsModel value.
     */
    @Generated
    public String getSameAsModel() {
        return this.sameAsModel;
    }

    /**
     * {@inheritDoc}
     */
    @Generated
    @Override
    public JsonWriter toJson(JsonWriter jsonWriter) throws IOException {
        jsonWriter.writeStartObject();
        jsonWriter.writeStringField("SameAsModel", this.sameAsModel);
        return jsonWriter.writeEndObject();
    }

    /**
     * Reads an instance of SameAsModel from the JsonReader.
     * 
     * @param jsonReader The JsonReader being read.
     * @return An instance of SameAsModel if the JsonReader was pointing to an instance of it, or null if it was
     * pointing to JSON null.
     * @throws IllegalStateException If the deserialized JSON object was missing any required properties.
     * @throws IOException If an error occurs while reading the SameAsModel.
     */
    @Generated
    public static SameAsModel fromJson(JsonReader jsonReader) throws IOException {
        return jsonReader.readObject(reader -> {
            String sameAsModel = null;
            while (reader.nextToken() != JsonToken.END_OBJECT) {
                String fieldName = reader.getFieldName();
                reader.nextToken();

                if ("SameAsModel".equals(fieldName)) {
                    sameAsModel = reader.getString();
                } else {
                    reader.skipChildren();
                }
            }
            return new SameAsModel(sameAsModel);
        });
    }
}