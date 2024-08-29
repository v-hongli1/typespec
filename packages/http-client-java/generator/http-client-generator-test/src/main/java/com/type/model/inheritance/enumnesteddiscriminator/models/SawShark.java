// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) TypeSpec Code Generator.

package com.type.model.inheritance.enumnesteddiscriminator.models;

import com.azure.core.annotation.Generated;
import com.azure.core.annotation.Immutable;
import com.azure.json.JsonReader;
import com.azure.json.JsonToken;
import com.azure.json.JsonWriter;
import java.io.IOException;

/**
 * The third level model SawShark in polymorphic multiple levels inheritance.
 */
@Immutable
public final class SawShark extends Shark {
    /**
     * Creates an instance of SawShark class.
     * 
     * @param age the age value to set.
     */
    @Generated
    public SawShark(int age) {
        super(age);
        this.kind = FishKind.SHARK;
        this.sharktype = SharkKind.SAW;
    }

    /**
     * {@inheritDoc}
     */
    @Generated
    @Override
    public JsonWriter toJson(JsonWriter jsonWriter) throws IOException {
        jsonWriter.writeStartObject();
        toJsonShared(jsonWriter);
        return jsonWriter.writeEndObject();
    }

    /**
     * Reads an instance of SawShark from the JsonReader.
     * 
     * @param jsonReader The JsonReader being read.
     * @return An instance of SawShark if the JsonReader was pointing to an instance of it, or null if it was pointing
     * to JSON null.
     * @throws IllegalStateException If the deserialized JSON object was missing any required properties.
     * @throws IOException If an error occurs while reading the SawShark.
     */
    @Generated
    public static SawShark fromJson(JsonReader jsonReader) throws IOException {
        return jsonReader.readObject(reader -> {
            int age = 0;
            SharkKind sharktype = SharkKind.SAW;
            while (reader.nextToken() != JsonToken.END_OBJECT) {
                String fieldName = reader.getFieldName();
                reader.nextToken();

                if ("age".equals(fieldName)) {
                    age = reader.getInt();
                } else if ("sharktype".equals(fieldName)) {
                    sharktype = SharkKind.fromString(reader.getString());
                } else {
                    reader.skipChildren();
                }
            }
            SawShark deserializedSawShark = new SawShark(age);
            deserializedSawShark.sharktype = sharktype;

            return deserializedSawShark;
        });
    }
}