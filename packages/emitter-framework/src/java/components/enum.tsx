import { mapJoin } from "@alloy-js/core";
import * as jv from "@alloy-js/java";
import { Enum } from "@typespec/compiler";

export interface EnumProps {
  type: Enum;
}

export function EnumDeclaration({ type }: EnumProps) {
  const members = Array.from(type.members.values());

  let valueType: string | undefined;
  let isConsistent = true;

  members.forEach((member, index) => {
    if (member.value !== undefined && member.value !== null) {
      const currentType = typeof member.value === "string" ? "String" : "int";

      if (valueType === undefined) {
        valueType = currentType;
      } else if (valueType !== currentType) {
        isConsistent = false;
      }
    }
  });

  // TypeSpec allows you to mix and match values, for a Java enum have to have one value
  if (!isConsistent) {
    throw new Error("All enum values must have the same type");
  }

  let constructor = null;
  let variable = null;
  let getter = null;
  if (valueType) {
    variable = <jv.Variable type={valueType} name="value" private={true} />;
    getter = (
      <jv.Method name={"getValue"} return={valueType} public>
        return this.value;
      </jv.Method>
    );

    constructor = (
      <jv.Constructor name={type.name} parameters={{ value: valueType }} private>
        this.value = value;
      </jv.Constructor>
    );
  }

  const joinedMembers = mapJoin(
    members,
    (member) => {
      let value;
      if (valueType) {
        value = <jv.Value value={member.value} />;
      } else {
        value = "";
      }
      return <jv.EnumMember name={member.name} arguments={value} />;
    },
    { joiner: ",\n" },
  );

  // prettier-ignore
  return valueType ? <jv.Enum name={type.name}>
    {joinedMembers};

    {variable}

    {getter}

    {constructor}
  </jv.Enum> : <jv.Enum name={type.name}>
    {joinedMembers}
  </jv.Enum>
}