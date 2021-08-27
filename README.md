# combinatorial_circuit_tester
  <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-release-plugin</artifactId>
        <version>3.0.0-M4</version>
        <configuration>
            <preparationGoals>resources:copy-resources@readme scm:add -Dincludes=README.md</preparationGoals>
            <completionGoals>resources:copy-resources@readme scm:add -Dincludes=README.md</completionGoals>
        </configuration>
    </plugin>
