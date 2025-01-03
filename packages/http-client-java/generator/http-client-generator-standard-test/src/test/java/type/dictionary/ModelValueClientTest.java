// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

package type.dictionary;

import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class ModelValueClientTest {

    ModelValueClient client = new DictionaryClientBuilder().buildModelValueClient();

    @Test
    @Disabled("type.dictionary.InnerModel is in unnamed module of loader 'app'")
    void get() {
        Map<String, InnerModel> response = client.get();
        Assertions.assertTrue(response.containsKey("k1"));
        InnerModel innerModel1 = response.get("k1");
        Assertions.assertEquals("hello", innerModel1.getProperty());
        Assertions.assertEquals(null, innerModel1.getChildren());

        Assertions.assertTrue(response.containsKey("k2"));
        InnerModel innerModel2 = response.get("k2");
        Assertions.assertEquals(null, innerModel2.getChildren());

    }

    @Test
    void put() {
        Map<String, InnerModel> map = new HashMap<>();
        InnerModel innerModel1 = new InnerModel("hello");
        map.put("k1", innerModel1);
        InnerModel innerModel2 = new InnerModel("world");
        map.put("k2", innerModel2);
        client.put(map);
    }
}